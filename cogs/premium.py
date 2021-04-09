import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


import sqlite3

db = sqlite3.connect('./DB/premium/premium.py')
cursor = db.cursor()


class Premium(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.guild_only()
	async def donate(self, ctx):
		await ctx.send(embed=discord.Embed(title= "Ошибка!", description=f"Команда находится в разработке", colour= config.ERR_COLOR))

def setup(client):
	client.add_cog(Premium(client))
	print('[Cog] Premium загружен!')