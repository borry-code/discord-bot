import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config



class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Ban
	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx,member:discord.Member,*,reason):
		emb = discord.Embed(title="Бан",color=config.ERR_COLOR)
		emb.add_field(name='Модератор',value = ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value = member.mention,inline=False)
		emb.add_field(name='Причина',value = reason,inline=False)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await member.ban(reason=reason)
		await ctx.send(embed = emb)



	#Clear
	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx,amount:int):
		if amount > 50:
			await ctx.send("За раз можно удалить максимум 50 сообщений")
		else:
			await ctx.channel.purge(limit=amount + 1)
			emb = discord.Embed(title= "Отчистка сообщений", description = f"{ctx.author.mention} удалил {amount} сообщений" , colour= config.MAIN_COLOR)
			emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
			await ctx.send(embed = emb)


	#Kick
	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx,member:discord.Member,reason):
		emb = discord.Embed(title="Кик",color=config.ERR_COLOR)
		emb.add_field(name='Модератор',value = ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value = member.mention,inline=False)
		emb.add_field(name='Причина',value = reason,inline=False)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await member.kick()
		await ctx.send(embed = emb)



def setup(client):
	client.add_cog(Moderation(client))
	print('[Cog] Moderation загружен!')