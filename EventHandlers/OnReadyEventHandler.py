import discord
from Commands import *
from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights import playerStore
from scorch_api.Applications import *


@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	if DEV_MODE: 
		# await bot.get_channel(944886185136894002).send("Development in this server has been (Re-)Enabled!")
		await runTests()
	else: 
		await sendMessageAsTelofik(f'In-Game Commands have been (Re-)Enabled!')
		await startApplicationMessage()
		await sendApplicationList()
	
async def runTests():
	channel = bot.get_channel(DEBUG_CHANNEL)
	all = 0
	succeeded = 0
	commands = {
		"refreshAll": refreshAllCommand,
		"anarchy": anarchyCommand,
		"bad": badCommand,
		"bdWeight": bdWeightCommand,
		"check": checkCommand,
		"health": healthCommand,
		"maxStats": maxStatsCommand,
		"me": meCommand,
		"parkour": parkourCommand,
		"sus": susCommand,
		"top": topCommand,
		"topAll": topAllCommand,
		"weight": weightCommand
	}

	embed = discord.Embed(title=f"RUNNING TESTS", color=discord.Color.blue())
	
	for command in commands: 
		embed.add_field(name=f"{command} - discord", value="⛔ in queue")
		embed.add_field(name=f"{command} - minecraft", value="⛔ in queue")

	embed.add_field(name="Succeeded:", value=f"{succeeded}/{all}")
	msg = await channel.send(embed=embed)	

	index = 0
	for command in commands:
		embed.set_field_at(index=index, name=f"{command}", value="<a:loading:960534697652396102> in progress")
		await msg.edit(embed=embed)
		command_object = commands[command]
		all+=2
		try: 
			command_object.discordMessage("ScorchChamp")
			succeeded += 1
			embed.set_field_at(index=index, name=f"{command} - discord", value="✅ test succeeded!")
		except Exception as e: 
			embed.set_field_at(index=index, name=f"{command} - discord", value="❌ test failed...")
			await channel.send(embed=discord.Embed(title=f"{str(command)} - discord: Test Failed...", description=e, color=discord.Color.red()))	
		
		index+=1
		try: 
			command_object.minecraftMessage("ScorchChamp")
			succeeded += 1
			embed.set_field_at(index=index, name=f"{command} - minecraft", value="✅ test succeeded!")
		except Exception as e: 
			embed.set_field_at(index=index, name=f"{command} - minecraft", value="❌ test failed...")
			await channel.send(embed=discord.Embed(title=f"{str(command)} - minecraft: Test Failed...", description=e, color=discord.Color.red()))	
		
		index+=1
		embed.set_field_at(index=len(commands)*2, name="Succeeded:", value=f"{succeeded}/{all}")
		await msg.edit(embed=embed)
