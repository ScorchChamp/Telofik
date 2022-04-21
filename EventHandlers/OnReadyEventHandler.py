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

	


	types = ["discord", "minecraft"]

	for type in types: 
		embed = discord.Embed(title=f"RUNNING TESTS FOR: {type}", color=discord.Color.blue())
		for command in commands: 
			embed.add_field(name=f"{command} - {type}", value="⛔ in queue")
		embed.add_field(name="Succeeded:", value=f"{succeeded}/{all}")
		msg = await channel.send(embed=embed)	
		for index in range(len(commands)):
			command = list(commands.keys())[index]
			embed.set_field_at(index=index, name=f"{command}", value="<a:loading:960534697652396102> in progress")
			await msg.edit(embed=embed)
			command_object = commands[command]
			all+=1
			try:
				if type=="discord": command_object.discordMessage("ScorchChamp")
				if type=="mniecraft": command_object.minecraftMessage("ScorchChamp")
				embed.set_field_at(index=index, name=f"{command} - {type}", value="✅ test succeeded!")
				succeeded+=1
			except Exception as e:
				embed.set_field_at(index=index, name=f"{command} - {type}", value="❌ test failed...")
				await channel.send(embed=discord.Embed(title=f"{str(command)} - {type}: Test Failed...", description=e, color=discord.Color.red()))	
			embed.set_field_at(index=len(commands), name="Succeeded:", value=f"{succeeded}/{all}")
			await msg.edit(embed=embed)
