from scorch_api.bot import *
import Utilities.WeightAPI as WeightAPI
			

def discordMessage(username, check_name = ""):   return BMC.newMessage(title=minecraftMessage(username, check_name))
def minecraftMessage(username, check_name = ""): 
    if check_name == "":
        if DEV_MODE:
            check_name = "ScorchChamp"
        else: return "Missing name! (do s+check 'username')"
    try: return f"{username}, {check_name}'s weight: {WeightAPI.getWeight(check_name)}"
    except: return f"{username}, Something went wrong!"
