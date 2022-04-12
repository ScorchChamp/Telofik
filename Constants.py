import os
from scorch_api.BotMessageCreator import BotMessageCreator
import functools
import typing
import asyncio


def to_thread(func: typing.Callable) -> typing.Coroutine:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper

APPLICATION_CHANNEL = 927969522051334185
APPLICATION_TITLE = "Stranded Sweats Application Form"
APPLICATION_DESC = "Press the button below to submit an application! \
	\n\n **The minimum Stranded weight requirement is: {}.** \
	\n\nIf your weight is below this limit, your application will be automatically rejected! (Check your weight by doing s+weight)"
APPLICATION_LIST_TITLE = "Application Queue List!"
MINIMUM_WEIGHT = 2500
CHECK_EMOJI = "✅"
CROSS_EMOJI = "❌"

DEV_MODE = True
API_BASE = 'http://192.168.1.100:8880/api'
SWEATS_BRIDGE_CHANNEL = 932028296097583134
DEBUG_CHANNEL = 958739798015758347
DEBUG_USER = "ScorchChamp"

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = BASE_PATH + "/data/"
if not os.path.exists(DATA_PATH): os.makedirs(DATA_PATH)
WHITELIST = DATA_PATH + "/whitelist.json"

SUSY_BAKAS = ["scorchchamp", "dante__daddy", "telofik"]

NO_PERSONALIZED_MESSAGE = "LMAO %s, apparently you are not popular enough for a personalized message xd"
MESSAGE_JSON = DATA_PATH + "/messages.json"
BMC = BotMessageCreator(name="SSG Bot by Scorch#8227 (ScorchChamp)", version="v2.0")


RATIO_MESSAGE = "{}: you fell off + ratio + you're white + you're british + who asked + no u + deez nuts + radio + don't care + didn't ask + i'm a minor + i'm neurodivergent + caught in 4k + cope + seethe + GG + your mom's + grow up + L + L (part 2) + retweet + ligma + taco bell tortilla crunch + think outside the bun + ur benched + ur a wrench + i own you + ur dad fell off + my dad could beat ur dad up + ur aimhacking + silver elite + tryhard + boomer + sksksksk + ur beta + i'm sigma + ur submissive + L (part 3) + yb better + ur sus + this is a cry for help and i'm extremely depressed. + quote tweet + you're cringe + i did your mom + you bought monkey nft + you're weirdchamp + you're a clown + my father left me at the age of 4 and i never recovered since + my dad owns steam + who want me? + i'm lonely + they didn't think it could possibly happen, but they're releasing L (part 5)".upper()
ANARCHY_MESSAGE = f'ScorchChamp is doing this for free, so might as well plug his anarchy superflat world: anarchy.scorchchamp.com (1.18.2). First to get the dragon gets discord nitro :)'

HELP_MESSAGE = "\
s+weight	\
s+me	\
s+health	\
s+bad	\
s+anarchy	\
s+sus	\
s+refreshall (Scorch ONLY!)	\
s+parkour	\
s+top	\
s+topall	\
s+help	\
s+ratio   \
s+bdweight   \
s+check"


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
STORE = DATA_PATH + "/player_data.json"
WEIGHT_PARTS = DATA_PATH + "/weight_parts.json"

if not os.path.isfile(MESSAGE_JSON):
	with open(MESSAGE_JSON, "w") as f:
		f.write('{"texts": [], "personalized_texts": {}}')

if not os.path.isfile(WHITELIST):
	with open(WHITELIST, "w") as f:
		f.write("[]")

if not os.path.isfile(WEIGHT_PARTS):
	with open(WEIGHT_PARTS, "w") as f:
		f.write("[]")


if not os.path.isfile(STORE):
	with open(STORE, "w") as f:
		f.write("{}")

