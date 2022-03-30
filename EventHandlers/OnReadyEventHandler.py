import discord
from scorch_api.bot import *
from Utilities.BridgeAPI import *
from Utilities.WeightAPI import *
from Utilities.Weights import playerStore
from scorch_api.Applications import *
import threading, asyncio


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await sendMessageAsTelofik(f'In-Game Commands have been (Re-)Enabled!')

    await startApplicationMessage()
    await sendApplicationList()
    # _thread = threading.Thread(target=asyncio.run, args=(playerStore.refreshAllPlayersInGuild(),))
    # _thread.start()