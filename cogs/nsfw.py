import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


import nekos

class NSFW(commands.Cog):
	def __init__(self, client):
		self.client = client

	#Cum
	@commands.command()
	@commands.guild_only()
	@commands.is_nsfw()
	async def cum(self, ctx):
		emb = discord.Embed(color = config.MAIN_COLOR)
		emb.set_image(url = nekos.img('cum'))
		await ctx.send(embed = emb)

	#Anal
	@commands.command()
	@commands.guild_only()
	@commands.is_nsfw()
	async def anal(self, ctx):
		emb = discord.Embed(color = config.MAIN_COLOR)
		emb.set_image(url = nekos.img('anal'))
		await ctx.send(embed = emb)

	#Tits
	@commands.command()
	@commands.guild_only()
	@commands.is_nsfw()
	async def tits(self, ctx):
		emb = discord.Embed(color = config.MAIN_COLOR)
		emb.set_image(url = nekos.img('tits'))
		await ctx.send(embed = emb)

	#Pussy
	@commands.command()
	@commands.guild_only()
	@commands.is_nsfw()
	async def pussy(self, ctx):
		emb = discord.Embed(color = config.MAIN_COLOR)
		emb.set_image(url = nekos.img('pussy_jpg'))
		await ctx.send(embed = emb)

	#nsfw_random
	@commands.command()
	@commands.guild_only()
	@commands.is_nsfw()
	async def nsfw_random(self, ctx):
		emb = discord.Embed(color = config.MAIN_COLOR)
		emb.set_image(url = nekos.img('random_hentai_gif'))
		await ctx.send(embed = emb)





def setup(client):
    client.add_cog(NSFW(client))
    print('[Cog] NSFW загружен!')