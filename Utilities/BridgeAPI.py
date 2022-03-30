import requests
import json
import random
import os
from scorch_api.bot import *

API_KEY = os.getenv('TELOFIK_API_AUTH')

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
MESSAGE_JSON = BASE_PATH + "/messages.json"
SWEATS_BRIDGE_CHANNEL = 932028296097583134

async def sendMessageAsTelofik(message):
    channel = bot.get_channel(SWEATS_BRIDGE_CHANNEL)
    await channel.send(embed=BMC.newMessage(title=message[:250]).getEmbed())
    requests.post('http://192.168.1.100:8880/api/sendmessage', data={"message": message}, headers={"authorization": API_KEY})

async def whisperAsTelofik(message, username):
    requests.post('http://192.168.1.100:8880/api/whisper', data={"message": message, "username": username}, headers={"authorization": API_KEY})


def getPlayerMeMessage(username):
    with open(MESSAGE_JSON, 'r') as file:
        data = json.load(file)
        if username in data['personalized_texts']: return data['personalized_texts'][username]
        else: return f"LMAO {username}, apparently you are not popular enough for a personalized message xd"

def getHealthMessage():
    with open(MESSAGE_JSON, 'r') as file:
        data = json.load(file)
        return random.choice(data['texts'])

def kickPlayerFromGuild(username):
    requests.post('http://192.168.1.100:8880/api/kick', data={"username": username}, headers={"authorization": API_KEY})
    
def invitePlayerToGuild(username):
    requests.post('http://192.168.1.100:8880/api/invite', data={"username": username}, headers={"authorization": API_KEY})
