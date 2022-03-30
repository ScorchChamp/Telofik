import Utilities.WeightAPI as WeightAPI
from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights.playerStore import *
from Utilities.PastebinAPI import *

@bot.command()
async def weight(ctx):
    score,breakdown = await WeightAPI.getWeight(ctx.author.display_name)
    await ctx.reply(embed=BMC.newMessage(title=f'Your STRANDED weight: {score}'))
    playerStore.storePlayerScore(ctx.author.display_name, score, breakdown)

@bot.command()
async def health(ctx):
    await ctx.reply(embed=BMC.newMessage(title='Healthy!'))

@bot.command()
async def bad(ctx):
    await ctx.reply(embed=BMC.newMessage(title=f'No U'))


@bot.command()
async def anarchy(ctx):
    await ctx.reply(embed=BMC.newMessage(title=f'ScorchChamp is doing this for free, so might as well plug his anarchy superflat world: anarchy.scorchchamp.com (1.18.2). First to get the dragon gets discord nitro :)'))

@bot.command()
async def bdweight(ctx):
    username = ctx.author.display_name
    await ctx.reply(embed=BMC.newMessage(title=f'{username}, your score breakdown:', description=await getBreakdownFormatted(username)))

@bot.command()
async def top(ctx):
    username = ctx.author.display_name
    placement, score = await playerStore.getSenitherPlacement(username)
    await ctx.reply(embed=BMC.newMessage(title=f'{username}, Your guild placement: {placement} with a score of {score["score"]}!'))

@bot.command()
async def topall(ctx):
    username = ctx.author.display_name
    data = await playerStore.getFullList()
    url = await pasteData(json.dumps(data, indent=4))
    await ctx.reply(embed=BMC.newMessage(title=f'Dear {username}, full list: {url}'))


@bot.command()
async def check(ctx, arg):
    try:
        score, breakdown = await WeightAPI.getWeight(arg)
        await ctx.reply(embed=BMC.newMessage(title=f'{arg}\'s STRANDED weight: {score}'))
        playerStore.storePlayerScore(ctx.author.display_name, score, breakdown)
    except:
        await ctx.reply(embed=BMC.newMessage(title=f'Something went wrong!'))

@bot.command()
async def maxStats(ctx):
    score, breakdown = await WeightAPI.maxStats()
    bd = '\n'.join([f"{item}: {breakdown[item]}" for item in breakdown])
    await ctx.reply(embed=BMC.newMessage(title=f'MAX Stats: (score: {score})', description=bd))
