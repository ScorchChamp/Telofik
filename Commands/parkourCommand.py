from scorch_api.bot import *

def discordMessage(username):   return BMC.newMessage(title=minecraftMessage(username))
def minecraftMessage(username): return f'{username} REMINDER TO DO YOUR PARKOUR!'
