import os
import json
import Utilities.WeightAPI as WeightAPI
import Utilities.HypixelAPI as HypixelAPI
import Utilities.MojangAPI as MojangAPI
from Utilities.BridgeAPI import *
import asyncio

from dotenv import load_dotenv, dotenv_values
load_dotenv()
STRANDED_SWEATS_GUILD_ID = dotenv_values('.env')["STRANDED_SWEATS_GUILD_ID"]

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
STORE = BASE_PATH + "/player_data.json"

def storePlayerScore(playername: str, score, breakdown):
	playername = playername.lower()
	with open(STORE, 'r') as file: data = json.load(file)
	data[playername] = {}
	data[playername]["score"] = float(score)
	data[playername]["breakdown"] = breakdown
	data = dict(sorted(data.items(), key=lambda item: item[1]["score"], reverse=True))
	with open(STORE, 'w') as file: file.write(json.dumps(data, indent=4))


async def refreshAllPlayersInGuild():
	uuids = await HypixelAPI.getAllPlayersInGuild(STRANDED_SWEATS_GUILD_ID)
	for uuid in uuids:
		playername = await MojangAPI.getUsernameFromUUID(uuid)
		print(playername)
		try:
			score, breakdown = await WeightAPI.getWeightUUID(uuid)
			storePlayerScore(playername, score, breakdown)
		except:
			storePlayerScore(playername, 0, {})
	await sendMessageAsTelofik(f'Refreshing Done!')
	
async def getFullList():
	with open(STORE, 'r') as file: 
		data = json.load(file)
		return data
	

async def getSenitherPlacement(playername):
	playername = str(playername).lower()
	score, breakdown = await WeightAPI.getWeight(playername)
	storePlayerScore(playername, score, breakdown)
	index = 0
	with open(STORE, 'r') as file: 
		data = json.load(file)
		for player in data:
			index += 1
			if player == playername: return index, data[player]
	return (0,{"score": -1})