from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights import playerStore
from Commands import *
from Utilities.PastebinAPI import *
import threading
import asyncio
import random



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
		if 's+sus' in desc: 		await sendMessageAsTelofik(susCommand.minecraftMessage(username))
		if 's+refreshall' in desc: 	await sendMessageAsTelofik(refreshAllCommand.minecraftMessage(username))
		if 's+parkour' in desc: 	await sendMessageAsTelofik(parkourCommand.minecraftMessage(username))
		if 's+bdweight' in desc: 	await sendMessageAsTelofik(bdWeightCommand.minecraftMessage(username))
		if 's+topall' in desc: 		await sendMessageAsTelofik(topAllCommand.minecraftMessage(username))
		if 's+weight' in desc: 		await sendMessageAsTelofik(weightCommand.minecraftMessage(username))
		if 's+me' in desc: 			await sendMessageAsTelofik(meCommand.minecraftMessage(username))
		if 's+health' in desc: 		await sendMessageAsTelofik(healthCommand.minecraftMessage(username))
		if 's+bad' in desc: 		await whisperAsTelofik(f'No u {username}', username)
		if 's+anarchy' in desc: 	await sendMessageAsTelofik(anarchyCommand.minecraftMessage(username))
		if 's+help' in desc: 		await sendMessageAsTelofik(HELP_MESSAGE)
		if 's+ratio' in desc: 		await sendMessageAsTelofik(RATIO_MESSAGE.format(username))
		if 's+top' in desc: 		await sendMessageAsTelofik(topCommand.minecraftMessage(username))
		if 's+check' in desc:		await sendMessageAsTelofik(checkCommand.minecraftMessage(username, desc.split("s+check")[1]))
		if 's+maxstats' in desc: 	await sendMessageAsTelofik(maxStatsCommand.minecraftMessage(username))