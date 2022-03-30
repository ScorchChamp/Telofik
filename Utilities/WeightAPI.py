import Utilities.HypixelAPI as HypixelAPI
import Utilities.MojangAPI as MojangAPI
import Utilities.Weights.playerStore as playerStore
from dotenv import load_dotenv, dotenv_values
import time
import json
import os
load_dotenv()
API_KEY = dotenv_values('.env')["API_KEY"]
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

async def getBreakdownFormatted(username):
	breakdown = (await getWeight(username))[1]
	return '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])

async def getBreakdownMAXFormatted():
	score, breakdown = await maxStats()
	return '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])



async def getWeightUUID(uuid):
	if not uuid: return (0,{})
	try: stranded_data = await HypixelAPI.getStrandedData(uuid)
	except: return (0, {})
	try:
		weights = [getStrandedWeight(member_data["members"][uuid]) for member_data in stranded_data]
		if not len(weights): return (0,{})
		return max(weights)
	except Exception as e:
		print(e)
		print("Something went wrong while retrieving the max weight!")
		return (0,{})

async def getWeight(username):
	uuid = await MojangAPI.getUUIDFromUsername(username)
	if not uuid: return (0,{})
	weight, breakdown = await getWeightUUID(uuid)
	playerStore.storePlayerScore(username, weight, breakdown)
	return weight, breakdown

async def maxStats():
	weight_parts, totalTime, max_score = generateWeightParts()
	res = {}
	for part in weight_parts: res[part['name']] = round((part["real_time"] / totalTime) * max_score)
	return max_score, res

def generateWeightParts():
	with open(BASE_DIR + "/weight_parts.json", "r") as f: weight_parts = json.load(f)
	for part in weight_parts: 
		part["time"] = part["maxXP"] / part["XPh"]
		part["real_time"] = (part["time"] * part["effort"]) + part["matGather"]
		if part["name"] == "minions": part["maxXP"] = part["maxXP"] ** 3
	return weight_parts, sum([part["real_time"] for part in weight_parts]), 100000

def getStrandedWeight(profileData):
	weight_parts, totalTime, max_score = generateWeightParts()
	score_breakdown = {}
	total_score = 0

	for part in weight_parts:
		name = str(part["name"]).lower() 
		if name == "minions": 
			xp_name = len(profileData[f"crafted_generators"]) ** 3
			score_breakdown[name] = round((part["real_time"] / totalTime) * max_score * (xp_name / part["maxXP"]))
		else: 
			try: xp_name = profileData[f"experience_skill_{name}"]
			except:
				try: xp_name = profileData["slayer_bosses"][name]["xp"]
				except: xp_name = 0
			score_breakdown[name] = round((part["real_time"] / totalTime) * max_score * (xp_name / part["maxXP"]))
		total_score += score_breakdown[name]
	return round(total_score), score_breakdown