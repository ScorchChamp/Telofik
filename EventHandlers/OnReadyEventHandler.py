import discord
from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights import playerStore
from scorch_api.Applications import *


@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	if DEV_MODE: 
		await bot.get_channel(944886185136894002).send("Development in this server has been (Re-)Enabled!")
		await runTests()
	else: 
		await sendMessageAsTelofik(f'In-Game Commands have been (Re-)Enabled!')
		await startApplicationMessage()
		await sendApplicationList()

	
async def runTests():
	channel = bot.get_channel(DEBUG_CHANNEL)
	placement, score = await playerStore.getSenitherPlacement(DEBUG_USER)
	await channel.send(embed=BMC.newMessage(title=f'{DEBUG_USER}, Your guild placement: {placement} with a score of {score["score"]}!'))
	await channel.send(embed=BMC.newMessage(title=(await WeightAPI.getWeight(DEBUG_USER))[0]))
	await channel.send(embed=BMC.newMessage(title='Healthy!'))
	await channel.send(embed=BMC.newMessage(title='No U!'))	
	await channel.send(embed=BMC.newMessage(title=f'ScorchChamp is doing this for free, so might as well plug his anarchy superflat world: anarchy.scorchchamp.com (1.18.2). First to get the dragon gets discord nitro :)'))
	await channel.send(embed=BMC.newMessage(title=f'{DEBUG_USER}, your score breakdown:', description=await getBreakdownFormatted(DEBUG_USER)))
	await channel.send(embed=BMC.newMessage(title=f'Dear {DEBUG_USER}, full list: {await PastebinAPI.pasteStoreData()}'))
	await channel.send(embed=BMC.newMessage(title=f'MAX Stats:', description=await getBreakdownMAXFormatted()))
	try: await channel.send(embed=BMC.newMessage(title=f'Lascivi\'s STRANDED weight: {(await WeightAPI.getWeight("Lascivi"))[0]}'))
	except: await channel.send(embed=BMC.newMessage(title=f'Something went wrong while retrieving weight for player!'))
	await channel.send(embed=BMC.newMessage(title=f'If you see this, all the tests probably succeeded!', color=discord.Color.green()))
