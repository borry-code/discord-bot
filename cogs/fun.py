import discord
from discord.ext import commands
from discord.ext.commands import Bot

import requests
import json
import random
import config


answers = ["Конечно!", "Можешь быть уверен(а)","Возмжно!","Нет!","Никак нет!", "Не думаю!"]


class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Bird
	@commands.command()
	@commands.guild_only()
	async def bird(self, ctx):
		response = requests.get('https://some-random-api.ml/img/birb')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":bird:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)


	
	#Cat
	@commands.command()
	@commands.guild_only()
	async def cat(self, ctx):
		response = requests.get('https://some-random-api.ml/img/cat')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":cat:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)


	
	#Dog
	@commands.command()
	@commands.guild_only()
	async def dog(self, ctx):
		response = requests.get('https://some-random-api.ml/img/dog')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":dog:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	
	#Fox
	@commands.command()
	@commands.guild_only()
	async def fox(self, ctx):
		response = requests.get('https://some-random-api.ml/img/fox')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":fox:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	
	#Koala
	@commands.command()
	@commands.guild_only()
	async def koala(self, ctx):
		response = requests.get('https://some-random-api.ml/img/koala')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":koala:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	
	#Panda
	@commands.command()
	@commands.guild_only()
	async def panda(self, ctx):
		response = requests.get('https://some-random-api.ml/img/panda')
		json_data = json.loads(response.text)
		emb = discord.Embed(title = ":panda_face:",color =config.MAIN_COLOR)
		emb.set_image(url = json_data['link'])
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	
	#Dice
	@commands.command()
	@commands.guild_only()
	async def dice(self, ctx):
		await ctx.send(f"Вам выпало {random.randint(1,6)}")


	#8ball
	@commands.command()
	@commands.guild_only()
	async def eightball(self, ctx, arg=None):
		if arg == None:
			await ctx.send(embed=discord.Embed(title= "Вы не ввели вопрос!", colour= config.ERR_COLOR))
		else:
			embed = discord.Embed(title = "🔮 Магический шар", description = random.choice(answers), color = config.MAIN_COLOR)
			await ctx.send(embed = embed)


	#Hug
	@commands.command()
	@commands.guild_only()
	async def hug(self, ctx, member : discord.Member = None):
		response = requests.get('https://some-random-api.ml/animu/hug')
		json_data = json.loads(response.text)
		if member == None:
			embed = discord.Embed(title = f"{ctx.author} обнял'а {self.client.user.name}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(title = f"{ctx.author} обнял'а {member}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)


	#Wink
	@commands.command()
	@commands.guild_only()
	async def wink(self, ctx, member : discord.Member = None):
		response = requests.get('https://some-random-api.ml/animu/wink')
		json_data = json.loads(response.text)
		if member == None:
			embed = discord.Embed(title = f"{ctx.author} подмигнул'а {self.client.user.name}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(title = f"{ctx.author} подмигнул'а {member}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)


	#Pat
	@commands.command()
	@commands.guild_only()
	async def pat(self, ctx, member : discord.Member = None):
		response = requests.get('https://some-random-api.ml/animu/pat')
		json_data = json.loads(response.text)
		if member == None:
			embed = discord.Embed(title = f"{ctx.author} погладил'а {self.client.user.name}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(title = f"{ctx.author} погладил'а {member}",color =0x2196F3)
			embed.set_image(url = json_data['link'])
			await ctx.send(embed = embed)



def setup(client):
	client.add_cog(Fun(client))
	print('[Cog] Fun загружен!')