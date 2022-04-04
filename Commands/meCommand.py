from scorch_api.bot import *

NO_PERSONALIZED_MESSAGE = "LMAO %s, apparently you are not popular enough for a personalized message xd"
MESSAGE_JSON = getBasePath(__file__) + "/messages.json"

def getMessageData(): 
    with open(MESSAGE_JSON, 'r') as file: return json.load(file)

def getPlayerMeMessage(username):
    try: return getMessageData()['personalized_texts'][username]
    except: return NO_PERSONALIZED_MESSAGE % username

def discordMessage(username):   return BMC.newMessage(title=f'Dear {username}, {getPlayerMeMessage(username)}')
def minecraftMessage(username): return f'Dear {username}, {getPlayerMeMessage(username)}'
