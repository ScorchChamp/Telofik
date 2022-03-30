from discord.ext import commands
from scorch_api.BotMessageCreator import BotMessageCreator

bot = commands.Bot(command_prefix='s+')
BMC = BotMessageCreator(name="SSG Bot by Scorch#8227 (ScorchChamp)", version="v2.0")



@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')


def startBot(token):
    bot.run(token)
