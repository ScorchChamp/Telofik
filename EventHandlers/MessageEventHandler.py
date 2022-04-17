from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights import playerStore
from Commands import *
from Utilities.PastebinAPI import *
import threading
import asyncio
import random

help_message = "\
s+weight	\
s+me	\
s+health	\
s+bad	\
s+anarchy	\
s+sus	\
s+refreshall (Scorch ONLY!)	\
s+parkour	\
s+top	\
s+topall	\
s+help	\
s+ratio   \
s+bdweight   \
s+check"


@bot.event
async def on_message(message):
	if message.author == bot.user: await runTelofikMessage(message)
	if message.author.bot: return # Don't do anything if the author is a bot
	await bot.process_commands(message)



async def runTelofikMessage(message):
	for embed in message.embeds:
		if not embed.description: continue
		desc = "".join(embed.description.split(" ")).lower()
		username = embed.author.name
		if 's+sus' in desc: await sendMessageAsTelofik(susCommand.minecraftMessage(username))
		if 's+refreshall' in desc: await sendMessageAsTelofik(refreshAllCommand.minecraftMessage(username))
		if 's+parkour' in desc: await sendMessageAsTelofik(parkourCommand.minecraftMessage(username))
		
		if 's+bdweight' in desc: await sendMessageAsTelofik(bdWeightCommand.minecraftMessage(username))
		if 's+topall' in desc: await sendMessageAsTelofik(topAllCommand.minecraftMessage(username))
		if 's+weight' in desc: await sendMessageAsTelofik(f'{username}, Your STRANDED weight: {(	etWeight(username))[0]}. Holy crap ur bad')
		if 's+me' in desc: await sendMessageAsTelofik(meCommand.discordMessage(username))
		if 's+health' in desc: await sendMessageAsTelofik(healthCommand.minecraftMessage(username))
		if 's+bad' in desc: await whisperAsTelofik(f'No u {username}', username)
		if 's+anarchy' in desc: await sendMessageAsTelofik(f'ScorchChamp is doing this for free, so might as well plug his anarchy superflat world: anarchy.scorchchamp.com (1.18.2). First to get the dragon gets discord nitro :)')
		if 's+help' in desc: await sendMessageAsTelofik(help_message)
		if 's+ratio' in desc: await sendMessageAsTelofik(f"{username}: you fell off + ratio + you're white + you're british + who asked + no u + deez nuts + radio + don't care + didn't ask + i'm a minor + i'm neurodivergent + caught in 4k + cope + seethe + GG + your mom's + grow up + L + L (part 2) + retweet + ligma + taco bell tortilla crunch + think outside the bun + ur benched + ur a wrench + i own you + ur dad fell off + my dad could beat ur dad up + ur aimhacking + silver elite + tryhard + boomer + sksksksk + ur beta + i'm sigma + ur submissive + L (part 3) + yb better + ur sus + this is a cry for help and i'm extremely depressed. + quote tweet + you're cringe + i did your mom + you bought monkey nft + you're weirdchamp + you're a clown + my father left me at the age of 4 and i never recovered since + my dad owns steam + who want me? + i'm lonely + they didn't think it could possibly happen, but they're releasing L (part 5)".upper())
		

		if 's+top' in desc: 
			placement, score = await playerStore.getSenitherPlacement(username)
			await sendMessageAsTelofik(f'{username}, Your guild placement: {placement} with a score of {score["score"]}!')
		if 's+check' in desc:
			name = desc.split("s+check")[1]
			try: await sendMessageAsTelofik(f"{username}, {name}'s weight: {	etWeight(name)}")
			except: await sendMessageAsTelofik(f"{username}, Something went wrong!")
		if 's+maxstats' in desc: 
			score, breakdown = await maxStats()
			await sendMessageAsTelofik(f"MAX stats: (score: {score}), {breakdown}")

def getRandomKey():
	keys = "abcdefghijklmnopqrstuvwxyz1234567890-="
	return random.choice(keys)

def generateAntiSpam():
	return ""
	# string = "".join([getRandomKey() for key in range(24)])
	# return f"[ANTI SPAM {string}]"
