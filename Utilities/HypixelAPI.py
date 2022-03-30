import requests
import Utilities.MojangAPI as MojangAPI

from dotenv import load_dotenv, dotenv_values
load_dotenv()
API_KEY = dotenv_values('.env')["API_KEY"]

async def getStrandedData(uuid):
    try:
        res = requests.get('https://api.hypixel.net/skyblock/profiles', params={"key": API_KEY, "uuid": uuid})
        if res.status_code != 200: 
            return []
        res = res.json()
    except Exception as e:
        print("Something went wrong in the hypixel API!", uuid)
        return []
    try:
        res = res['profiles']
        return [profile for profile in res if 'game_mode' in profile and profile['game_mode'] == 'island']
    except:
        return []


async def getStrandedProfileIDsForPlayer(uuid):
    res = requests.get('https://api.hypixel.net/skyblock/profiles', params={"key": API_KEY, "uuid": uuid}).json()
    try:
        res = res['profiles']
        return [profile['profile_id'] for profile in res if 'game_mode' in profile and profile['game_mode'] == 'island']
    except:
        return []

async def getGuildData(guild_id):
    res = requests.get('https://api.hypixel.net/guild', params={"key": API_KEY, "id": guild_id}).json()
    return res

async def getAllPlayersInGuild(guild_id):
    data = await getGuildData(guild_id)
    return [member['uuid'] for member in data['guild']['members']]

async def getAllPlayerNamesInGuild(guild_id):
    uuids = await getAllPlayersInGuild(guild_id)
    return [await MojangAPI.getUsernameFromUUID(uuid) for uuid in uuids]