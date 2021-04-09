import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


import requests
import json


class Utility(commands.Cog):
	def __init__(self, client):
		self.client = client

	#Calc
	@commands.command()
	@commands.guild_only()
	async def calc(self, ctx, *,exp = None):
		if exp is None:
			await ctx.send(embed=discord.Embed(title= "Ошибка!", description=f"Укажите пример", colour= config.ERR_COLOR))
		else:
			link = 'http://api.mathjs.org/v4/'

			data = {"expr": [f"{exp}"]}

			try:
				re = requests.get(link, params=data)
				responce = re.json()

				emb = discord.Embed(title='Калькулятор', color = config.MAIN_COLOR)
				emb.add_field(name='Задача:', value=exp)
				emb.add_field(name='Решение:', value=str(responce))
				await ctx.send(embed=emb)
			except:
				await ctx.send(embed=discord.Embed(title= "Ошибка!", description=f"Нельзя использовать текст в примере", colour= config.ERR_COLOR))	


def setup(client):
	client.add_cog(Utility(client))
	print('[Cog] Utility загружен!')