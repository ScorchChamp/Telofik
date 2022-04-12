from scorch_api.bot import *
import Utilities.WeightAPI as WeightAPI
import Utilities.Weights.playerStore as playerStore

def runCommand(username):
	score, breakdown = WeightAPI.getWeight(username)
	playerStore.storePlayerScore(username, score, breakdown)
	return score

def discordMessage(username):   return BMC.newMessage(title=f'Your Stranded Weight: {runCommand(username)}')
def minecraftMessage(username): return f"Your Stranded Weight: {runCommand(username)}"
