import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config



class Status(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		await self.client.change_presence( status = discord.Status.online, activity = discord.Game( '-help | https://borrybot.space/' ) )

def setup(client):
	client.add_cog(Status(client))
	print('[Cog] Status загружен!')