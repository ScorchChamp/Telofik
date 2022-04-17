from scorch_api.bot import *
import Utilities.WeightAPI as WeightAPI

def discordMessage(username):   return BMC.newMessage(title=f'{username}, your score breakdown:', description = WeightAPI.getBreakdownFormatted(username))
def minecraftMessage(username): return f'{username}, your score breakdown: {WeightAPI.getWeight(username)[1]}'
