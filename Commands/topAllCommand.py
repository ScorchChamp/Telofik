from scorch_api.bot import *
import Utilities.PastebinAPI as PastebinAPI

def discordMessage(username):   return BMC.newMessage(title = f"Full top list: {PastebinAPI.pasteStoreData()}")
def minecraftMessage(username): return f'Dear {username}, full list: {PastebinAPI.pasteStoreData()}'