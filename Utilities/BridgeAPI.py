import requests
import json
import random
import os
from scorch_api.bot import *

API_KEY = os.getenv('TELOFIK_API_AUTH')
BASE_PATH = getBasePath(__file__)

MESSAGE_JSON = BASE_PATH + "/messages.json"

def getMessageData():
    with open(MESSAGE_JSON, 'r') as file: return json.load(file)

async def sendMessageAsTelofik(message):
    channel = bot.get_channel(SWEATS_BRIDGE_CHANNEL)
    await channel.send(embed=BMC.newMessage(title=message[:250]))
    sendAPIRequest('/sendmessage', {"message": message})

def getPlayerMeMessage(username):
    data = getMessageData()
    if username in data['personalized_texts']: return data['personalized_texts'][username]
    else: return f"LMAO {username}, apparently you are not popular enough for a personalized message xd"

def getHealthMessage():
    data = getMessageData()
    return random.choice(data['texts'])

def sendAPIRequest(endpoint, data): requests.post(f'{API_BASE}/{endpoint}', data=data, headers={"authorization": API_KEY})
def whisperAsTelofik(message, username): sendAPIRequest('/whisper', {"username": username, "message": message})
def kickPlayerFromGuild(username):  sendAPIRequest('/kick', {"username": username})
def invitePlayerToGuild(username):  sendAPIRequest('/invite', {"username": username})
