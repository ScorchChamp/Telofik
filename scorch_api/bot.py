from discord.ext import commands
import os
from Constants import *

bot = commands.Bot(command_prefix='s+')

def startBot(token): bot.run(token)
def getBasePath(file): return os.path.dirname(os.path.realpath(file))