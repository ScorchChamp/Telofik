import requests
import os
from scorch_api.bot import *

API_KEY = os.getenv('TELOFIK_API_AUTH')

async def sendMessageAsTelofik(message):
	await bot.get_channel(SWEATS_BRIDGE_CHANNEL).send(embed=BMC.newMessage(title=message[:250]))
	sendAPIRequest('sendmessage', {"message": message})


def sendAPIRequest(endpoint, data): requests.post(f'{API_BASE}/{endpoint}', data=data, headers={"authorization": API_KEY})
def whisperAsTelofik(message, username): sendAPIRequest('whisper', {"username": username, "message": message})
def kickPlayerFromGuild(username):  sendAPIRequest('kick', {"username": username})
def invitePlayerToGuild(username):  sendAPIRequest('invite', {"username": username})
