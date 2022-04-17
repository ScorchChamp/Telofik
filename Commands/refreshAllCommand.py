from scorch_api.bot import *
import Utilities.Weights.playerStore as playerStore
from threading import Thread

BASE_PATH = getBasePath(__file__)
			
def discordMessage(username): return BMC.newMessage(title=minecraftMessage(username))
def minecraftMessage(username): 
    if username.lower() != "scorchchamp": return f'Im sorry {username}, I dont think you can do that'
    else: 
        _thread = Thread(target=playerStore.refreshAllPlayersInGuild)
        _thread.start()

        _thread.join()

        return f'Refreshing guild values! This might take a while...'
