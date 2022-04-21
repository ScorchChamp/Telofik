from scorch_api.bot import *
import random

def discordMessage(username): return BMC.newMessage(title=minecraftMessage(username))
    
def minecraftMessage(username): 
	if random.randint(0,100) < 2 or username.lower() in SUSY_BAKAS: return f'{username}, youre the impostor.... sssh'
	else: return f'{username} is not sus'
