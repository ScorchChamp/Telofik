import requests
import Utilities.MojangAPI as MojangAPI

from dotenv import load_dotenv, dotenv_values
load_dotenv()
API_KEY = dotenv_values('.env')["API_KEY"]
HYPIXEL_API = "https://api.hypixel.net"

async def getStrandedData(uuid):
	try: res = getHypixelData("skyblock/profiles", {"uuid": uuid})
	except: return []
	try: return [profile for profile in res['profiles'] if 'game_mode' in profile and profile['game_mode'] == 'island']
	except: return []


async def getStrandedProfileIDsForPlayer(uuid):
	res = getHypixelData("skyblock/profiles", {"uuid": uuid})
	try: return [profile['profile_id'] for profile in res['profiles'] if 'game_mode' in profile and profile['game_mode'] == 'island']
	except: return []

async def getGuildData(guild_id): return getHypixelData("guild", {"id": guild_id})

async def getAllPlayersInGuild(guild_id):
	return [member['uuid'] for member in (await getGuildData(guild_id))['guild']['members']]

async def getAllPlayerNamesInGuild(guild_id):
	uuids = await getAllPlayersInGuild(guild_id)
	return [await MojangAPI.getUsernameFromUUID(uuid) for uuid in uuids]

def getHypixelData(endpoint, params):
	params["key"] = API_KEY
	return requests.get(f'{HYPIXEL_API}/{endpoint}', params=params).json()