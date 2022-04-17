import Utilities.HypixelAPI as HypixelAPI
import Utilities.MojangAPI as MojangAPI
import Utilities.Weights.playerStore as playerStore
from dotenv import load_dotenv, dotenv_values
import json
import os

load_dotenv()
API_KEY = dotenv_values('.env')["API_KEY"]
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def getBreakdownFormatted(username):
	breakdown = getWeight(username)[1]
	return '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])

def getBreakdownMAXFormatted():
	score, breakdown = maxStats()
	return '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])



def getWeightUUID(uuid):
	if not uuid: return (0,{})
	try: stranded_data = HypixelAPI.getStrandedData(uuid)
	except: return (0, {})
	try:
		weights = [getStrandedWeight(member_data["members"][uuid]) for member_data in stranded_data]
		if not len(weights): return (0,{})
		return max(weights)
	except Exception as e: return (0,{})

def getWeight(username):
	uuid = MojangAPI.getUUIDFromUsername(username)
	if not uuid: return (0,{})
	weight, breakdown = getWeightUUID(uuid)
	playerStore.storePlayerScore(username, weight, breakdown)
	return weight, breakdown

def maxStats(): return getStrandedWeight({}, max=True)

def generateWeightParts():
	with open(BASE_DIR + "/weight_parts.json", "r") as f: weight_parts = json.load(f)
	for part in weight_parts: 
		part["time"] = part["maxXP"] / part["XPh"]
		part["real_time"] = (part["time"] * part["effort"]) + part["coin_cost"]
		part["maxXP"] = part["maxXP"] ** part["curve"]
	return weight_parts, sum([part["real_time"] for part in weight_parts]), 100000

def getStrandedWeight(profileData, max = False):
	weight_parts, totalTime, max_score = generateWeightParts()
	score_breakdown = {}
	total_score = 0

	for part in weight_parts:
		name = str(part["name"]).lower() 
		if max: xp_name = part["maxXP"]
		else: 
			if name == "minions": xp_name = len(profileData[f"crafted_generators"])
			else: 
				try: xp_name = profileData[f"experience_skill_{name}"]
				except:
					try: xp_name = profileData["slayer_bosses"][name]["xp"]
					except: xp_name = 0
		xp_name = min(xp_name ** part["curve"], part["maxXP"])
		score_breakdown[name] = round((part["real_time"] / totalTime) * max_score * (xp_name / part["maxXP"]))
		total_score += score_breakdown[name]
	return round(total_score), score_breakdown