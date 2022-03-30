import os
import random
import time
import requests
import discord
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
import pathlib

PREFIX = 's+'
BASE_DIR = pathlib.Path(__file__).parent.resolve()
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('API_KEY')

client = discord.Client()
client = commands.Bot(command_prefix=PREFIX)

def getHealthMessage(username):
    return random.choice(random_texts)

def getMeMessage(username):
    if username in personalized_message: return personalized_message[username]
    else: return f"LMAO {username}, apparently you are not popular enough for a personalized message xd"

async def getTopWeights():
    return 'name', 0

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await sendMessageAsTelofik("In-Game Commands have been (re-)enabled!")

@client.command()
async def weight(ctx):
    await ctx.send(f'Your senither weight: {await getSenitherWeight(ctx.author.display_name)}')

@client.command()
async def health(ctx):
    await ctx.send('Healthy!')

@client.event
async def on_message(message):
    if message.embeds:
        for embed in message.embeds:
            if not embed.description: continue
            if 's+weight' in embed.description: await sendMessageAsTelofik(f'{embed.author.name}, Your senither weight: {await getSenitherWeight(embed.author.name)}. Imagine being that bad lmao')
            if 's+me' in embed.description: await sendMessageAsTelofik(getMeMessage(embed.author.name))
            if 's+health' in embed.description: await sendMessageAsTelofik(f'Dear {embed.author.name}, {getHealthMessage(embed.author.name)}')
            if 's+bad' in embed.description: await whisperAsTelofik(f'No u', embed.author.name)
            if 's+swavy' in embed.description: await sendMessageAsTelofik(f'Swavy is a rat that made a flatworld anarchy world once. ScorchChamp and Juenez absolutely DOMINATED that world')
            if 's+top' in embed.description: 
                await sendMessageAsTelofik(f'Hi {embed.author.name}, This command is currently disabled!')
                # await sendMessageAsTelofik(f'Hi {embed.author.name}, ill calculate that top now senpai <3')
                # top_name, top_weight = await getTopWeights()
                # time.sleep(2)
                # await sendMessageAsTelofik(f'OOP! {embed.author.name}, Something went wrong!')
    await client.process_commands(message)


async def sendMessageAsTelofik(message):
    requests.post('http://192.168.1.100:8880/api/sendmessage', data={"message": message}, headers={"authorization": "StrandedSweatsAuth"})

async def whisperAsTelofik(message, username):
    requests.post('http://192.168.1.100:8880/api/whisper', data={"message": message, "username": username}, headers={"authorization": "StrandedSweatsAuth"})

async def getUUIDFromUsername(username):
    return requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}').json()['id']

async def getSenitherWeight(username):
    uuid = await getUUIDFromUsername(username)
    valid_profileIDS = await getStrandedProfileIDsForPlayer(uuid)
    res = requests.get(f'https://hypixel-api.senither.com/v1/profiles/{uuid}', headers={"Authorization": API_KEY}).json()['data']
    for profile in res:
        if profile['id'] in valid_profileIDS:
            return "{:.2f}".format(profile['weight'])
    return 0

async def getStrandedProfileIDsForPlayer(uuid):
    res = requests.get('https://api.hypixel.net/skyblock/profiles', params={"key": API_KEY, "uuid": uuid}).json()
    res = res['profiles']
    return [profile['profile_id'] for profile in res if 'game_mode' in profile and profile['game_mode'] == 'island']


client.run(TOKEN)