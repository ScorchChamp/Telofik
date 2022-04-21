from scorch_api.bot import *
import Utilities.Weights.playerStore as playerStore

def discordMessage(username): return BMC.newMessage(title=minecraftMessage(username))
def minecraftMessage(username): 
    if username.lower() != "scorchchamp": return f'Im sorry {username}, I dont think you can do that'
    else: 
        bot.loop.create_task(playerStore.refreshAllPlayersInGuild())
        return 'Refreshing guild values! This might take a while...'
