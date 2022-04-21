from scorch_api.bot import *
import Utilities.WeightAPI as WeightAPI
			

def discordMessage(username):  return BMC.newMessage(title=minecraftMessage(username))
def minecraftMessage(username): 
    score, breakdown = WeightAPI.maxStats()
    return f"MAX stats: (score: {score}), {breakdown}"
