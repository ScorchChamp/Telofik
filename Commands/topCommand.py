from scorch_api.bot import *
import Utilities.Weights.playerStore as playerStore

def discordMessage(username):   return BMC.newMessage(title=f"Your guild placement: {playerStore.getStrandedPlacement(username)[0]}")
def minecraftMessage(username): return f"Dear {username}, Your guild placement: {playerStore.getStrandedPlacement(username)[0]}"