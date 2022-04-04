from scorch_api.bot import *

BASE_PATH = getBasePath(__file__)

def discordMessage(username):   return BMC.newMessage(title=minecraftMessage(username))
def minecraftMessage(username): return f'{username} REMINDER TO DO YOUR PARKOUR!'
