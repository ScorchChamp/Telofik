import requests


async def getUUIDFromUsername(username):
    data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
    return data.json()['id']

async def getUsernameFromUUID(uuid):
    res = requests.get(f'https://api.mojang.com/user/profiles/{uuid}/names').json()
    return res[len(res)-1]['name']
