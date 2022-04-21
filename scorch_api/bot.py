from discord.ext import commands
import os
from Constants import *

DEV_MODE = False
API_BASE = 'http://192.168.1.100:8880/api'
SWEATS_BRIDGE_CHANNEL = 932028296097583134
DEBUG_CHANNEL = 958739798015758347
DEBUG_USER = "ScorchChamp"

bot = commands.Bot(command_prefix='s+')

def startBot(token): bot.run(token)
def getBasePath(file): return os.path.dirname(os.path.realpath(file))