import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


class Support(commands.Cog):
	def __init__(self, client):
		self.client = client
		

	#Bug
	@commands.command()
	@commands.guild_only()
	@commands.cooldown(1, 10800, commands.BucketType.user)
	async def bug( self, ctx, *, bug ):
		channel = self.client.get_channel(BUG_CHANNEL)
		embed = discord.Embed(title = 'Баг отправлен!',description = f'Баг: {bug}',color = config.MAIN_COLOR)
		await ctx.send(embed = embed)
		emb = discord.Embed(title = 'Баг!', color = config.MAIN_COLOR)
		emb.add_field(name = "Баг:", value = bug, inline = False)
		emb.set_footer(text=f"Username:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}", icon_url = ctx.author.avatar_url)
		await channel.send(embed = emb)


	#Idea
	@commands.command()
	@commands.guild_only()
	@commands.cooldown(1, 10800, commands.BucketType.user)
	async def idea( self, ctx, *, idea ):
		channel = self.client.get_channel(IDEA_CHANNEL)
		embed = discord.Embed(title = 'Идея отправлена!',description = f'Идея: {idea}',color = config.MAIN_COLOR)
		await ctx.send(embed = embed)
		emb = discord.Embed(title = 'Идея!', color = config.MAIN_COLOR)
		emb.add_field(name = "Идея:", value = idea, inline = False)
		emb.set_footer(text=f"Username:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}", icon_url = ctx.author.avatar_url)
		await channel.send(embed = emb)


	#Invite
	@commands.command()
	@commands.guild_only()
	async def invite(self, ctx):
		emb = discord.Embed(title = "Добавить бота на свой сервер", color=config.MAIN_COLOR)
		emb.add_field(name=f'Приглашение Бота:',value="[Пригласить](https://discord.com/api/oauth2/authorize?client_id=749588703185338449&permissions=8&scope=bot)",inline=False)
		await ctx.send(embed = emb)


		
def setup(client):
	client.add_cog(Support(client))
	print('[Cog] Support загружен!')