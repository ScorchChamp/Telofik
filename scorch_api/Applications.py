from scorch_api.bot import *
import os
import json

APPLICATION_CHANNEL = 927969522051334185
APPLICATION_TITLE = "Stranded Sweats Application Form"
APPLICATION_DESC = "Press the button below to submit an application! \
	\n\n **The minimum Stranded weight requirement is: {}.** \
	\n\nIf your weight is below this limit, your application will be automatically rejected! (Check your weight by doing s+weight)"
APPLICATION_LIST_TITLE = "Application Queue List!"
MINIMUM_WEIGHT = 2500
CHECK_EMOJI = "✅"
CROSS_EMOJI = "❌"

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
WHITELIST = BASE_PATH + "/whitelist.json"

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