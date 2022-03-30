import requests
import json
import random
import os
from scorch_api.bot import *

API_KEY = os.getenv('TELOFIK_API_AUTH')
BASE_PATH = getBasePath(__file__)

NO_PERSONALIZED_MESSAGE = "LMAO %s, apparently you are not popular enough for a personalized message xd"
MESSAGE_JSON = BASE_PATH + "/messages.json"

def getMessageData():
	with open(MESSAGE_JSON, 'r') as file: return json.load(file)

async def sendMessageAsTelofik(message):
	await bot.get_channel(SWEATS_BRIDGE_CHANNEL).send(embed=BMC.newMessage(title=message[:250]))
	sendAPIRequest('sendmessage', {"message": message})

def getPlayerMeMessage(username):
	try: return getMessageData()['personalized_texts'][username]
	except: return NO_PERSONALIZED_MESSAGE % username

def getHealthMessage():
	return random.choice(getMessageData()['texts'])

def sendAPIRequest(endpoint, data): requests.post(f'{API_BASE}/{endpoint}', data=data, headers={"authorization": API_KEY})
def whisperAsTelofik(message, username): sendAPIRequest('whisper', {"username": username, "message": message})
def kickPlayerFromGuild(username):  sendAPIRequest('kick', {"username": username})
def invitePlayerToGuild(username):  sendAPIRequest('invite', {"username": username})
