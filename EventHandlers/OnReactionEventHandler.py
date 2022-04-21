from scorch_api.bot import *
from scorch_api.Applications import *
import Utilities.WeightAPI as WeightAPI
import Utilities.HypixelAPI as HypixelAPI
import Utilities.MojangAPI as MojangAPI
import json

from dotenv import load_dotenv, dotenv_values
load_dotenv()
STRANDED_SWEATS_GUILD_ID = dotenv_values('.env')["STRANDED_SWEATS_GUILD_ID"]


@bot.event
async def on_reaction_add(reaction, user):
	if user.bot: return
	if reaction.message.channel.id == APPLICATION_CHANNEL:
		print(user.name + " applied!")
		with open(WHITELIST, 'r') as file: data = json.load(file)
		if reaction.emoji == "✅":
			if user.display_name not in data: 
				await user.send(embed=BMC.newMessage(description="Your application to SSG has been received!"))
				weight, breakdown = await WeightAPI.getWeight(user.display_name)
				uuid = await MojangAPI.getUUIDFromUsername(user.display_name)
				if not uuid: await user.send(embed=BMC.newMessage(description="Your username was not found. Make sure your displayname is the same as your in-game name!"))
				elif uuid in await HypixelAPI.getAllPlayersInGuild(STRANDED_SWEATS_GUILD_ID):
					await user.send(embed=BMC.newMessage(description="Ayo sneaky. Youre already in this guild!"))
					print(user.name + " is already in guild!")
				elif float(weight) < MINIMUM_WEIGHT:
					await user.send(embed=BMC.newMessage(description="Your application to SSG has been REJECTED: **Your senither weight is too low!**"))
				
					print(user.name + " got rejected!")
				else: 
					data.append(user.display_name)
					print(user.name + " got added!")

		elif reaction.emoji == "❌":
			for i in range(len(data)):
				if data[i] == user.display_name: 
					print(user.name + " got removed!")
					data.pop(i)
					with open(WHITELIST, 'w') as file: file.write(json.dumps(data, indent=4))
		await reaction.remove(user)
	await updateChannelForApplications()