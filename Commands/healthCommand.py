from scorch_api.bot import *
import random
import json

def getMessageData(): 
    with open(MESSAGE_JSON, 'r') as file: return json.load(file)
def getHealthMessage(): return random.choice(getMessageData()['texts'])



def discordMessage(username):   return BMC.newMessage(title=getHealthMessage())
def minecraftMessage(username): return f"Dear {username}, {getHealthMessage()}"