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
        self.embed.set_footer(text=name + " " + version, icon_url="https://images-ext-2.discordapp.net/external/6h3wHPrvusV-c3Qym51q3AroTqRlVzylhmn1Dp-8cio/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/329996760053317632/effa3ffb2dd8730d5fa215d141835d90.png")
        return self.embed
        
