from scorch_api.bot import *
import os
import json

async def startApplicationMessage():
	await deleteOldApplicationMessages()
	channel = bot.get_channel(APPLICATION_CHANNEL)
	embed = BMC.newMessage(title=APPLICATION_TITLE, description=APPLICATION_DESC.format(MINIMUM_WEIGHT))
	message = await channel.send(embed=embed)
	await message.add_reaction(CHECK_EMOJI)
	await message.add_reaction(CROSS_EMOJI)

async def sendApplicationList():
	await bot.get_channel(APPLICATION_CHANNEL).send(embed = generateQueueList())

async def deleteOldApplicationMessages():
	channel = bot.get_channel(APPLICATION_CHANNEL)
	for message in channel.history(limit=2):
		if message.author == bot.user: await message.delete()

async def updateChannelForApplications():
	channel = bot.get_channel(APPLICATION_CHANNEL)
	for message in channel.history(limit=2):
		if message.author == bot.user:
			for embed in message.embeds: 
				if embed.title == APPLICATION_LIST_TITLE: await message.edit(embed = generateQueueList())


def generateQueueList():
	try:
		with open(WHITELIST, 'r') as file: data = json.load(file)
	except:
		with open(WHITELIST, 'w') as file: 
			file.write("[]")
			data = []

	desc = "\n".join([username for username in data])
	embed = BMC.newMessage(title=APPLICATION_LIST_TITLE, description=desc)
	return embed