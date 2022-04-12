from Commands import badCommand
import Utilities.WeightAPI as WeightAPI
import Utilities.PastebinAPI as pastebinAPI
from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights.playerStore import *
from Commands import *

@bot.command()
async def weight(ctx): await ctx.reply(embed=weightCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def health(ctx): await ctx.reply(embed=healthCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def bad(ctx): await ctx.reply(embed=badCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def me(ctx): await ctx.reply(embed=meCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def anarchy(ctx): await ctx.reply(embed=anarchyCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def bdweight(ctx): await ctx.reply(embed=bdWeightCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def top(ctx): await ctx.reply(embed=topCommand.discordMessage(ctx.author.display_name))

@bot.command()
async def topall(ctx):
	username = ctx.author.display_name
	data = await playerStore.getFullList()
	url = await pastebinAPI.pasteData(json.dumps(data, indent=4))
	await ctx.reply(embed=BMC.newMessage(title=f'Dear {username}, full list: {url}'))


@bot.command()
async def check(ctx, arg):
	try:
		score, breakdown = await WeightAPI.getWeight(arg)
		bd = '\n'.join([f"{name}: {breakdown[name]}" for name in breakdown])
		await ctx.reply(embed=BMC.newMessage(title=f'{arg}\'s STRANDED weight: {score}', description=bd))
		playerStore.storePlayerScore(arg, score, breakdown)
	except:
		await ctx.reply(embed=BMC.newMessage(title=f'Something went wrong!'))

@bot.command()
async def maxStats(ctx):
	score, breakdown = await WeightAPI.maxStats()
	bd = '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])
	await ctx.reply(embed=BMC.newMessage(title=f'MAX Stats: (score: {score})', description=bd))
