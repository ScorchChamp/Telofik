from scorch_api.bot import *
import random

BASE_PATH = getBasePath(__file__)
sussy_bakas = ["scorchchamp", "dante__daddy", "telofik"]

def discordMessage(username):
    return BMC.newMessage(title=minecraftMessage(username))
    
def minecraftMessage(username): 
	if random.randint(0,100) < 2 or username.lower() in sussy_bakas: return f'{username}, youre the impostor.... sssh'
	else: return f'{username} is not sus'
