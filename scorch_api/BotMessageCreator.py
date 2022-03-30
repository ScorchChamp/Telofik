from tkinter import W
import discord

class BotMessageCreator:    
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def newMessage(self, title:str = "", description: str = ""):
        message = BotMessage(name=self.name, version=self.version, description=description, title=title)
        return message



class BotMessage:
    embed = None
    def __init__(self, message: str = "", version: str = "v1.0", color: discord.Colour = discord.Colour.blue(), title: str = "", name: str = "", description: str = ""):
        self.embed = discord.Embed(title=title, description=description, colour=color)
        self.setFooter(text = name + " " + version)

    def setFooter(self, text: str, icon_url: str = ""):
        self.embed.set_footer(text=text, icon_url=icon_url)

    def getEmbed(self):
        return self.embed

