from tkinter import W
import discord

class BotMessageCreator:	
	def __init__(self, name: str, version: str):
			self.name = name
			self.version = version

	def newMessage(self, title:str = "", description: str = "", color = discord.Colour.blue()):
		description += "\n\n We are aware of any faulty Farming weights!"
		self.embed = discord.Embed(title=title, description=description, colour=color)
		self.embed.set_footer(text=self.name + " " + self.version, icon_url="https://images-ext-2.discordapp.net/external/6h3wHPrvusV-c3Qym51q3AroTqRlVzylhmn1Dp-8cio/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/329996760053317632/effa3ffb2dd8730d5fa215d141835d90.png")
		return self.embed

		
