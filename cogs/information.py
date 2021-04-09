import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


import psutil


class Information(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Info
	@commands.command()
	@commands.guild_only()
	async def info(self, ctx):

		guild_count = len(self.client.guilds)

		emb = discord.Embed(title=f"{self.client.user.name}#{self.client.user.discriminator}",description="Информация о боте **BorryBot**.\n",color=config.MAIN_COLOR)
		emb.add_field(name=f'Бота создал:', value="BORRY#5253", inline=True)
		emb.add_field(name=f'Серверов:', value=f"{guild_count}", inline=True)
		emb.add_field(name=f'Префикс бота:', value="-", inline=True)
		emb.add_field(name=f'Бот написан на:', value="Discord.py", inline=True)
		emb.add_field(name=f'Версия бота:', value="0.5(от 19.02.2021)", inline=True)
		emb.add_field(name=f'Язык бота:', value="Русский", inline=True)
		emb.add_field(name=f'Приглашение Бота:',value="[Пригласить](https://discord.com/api/oauth2/authorize?client_id=749588703185338449&permissions=8&scope=bot)",inline=True)
		emb.add_field(name=f'Сервер BorryBot Community:', value="[Вступить](https://discord.gg/CKyV4Vn)",inline=True)
		emb.add_field(name=f'Полезные ссылки:', value="[Сайт](https://borrybot.space/)\n[Сервер поддержки](https://discord.gg/CKyV4Vn)\n[Boosty](https://boosty.to/borrybot)\n[BotiCord.top](https://boticord.top/bot/749588703185338449)",inline=True)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	#Ping
	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):
		emb = discord.Embed(title= "Ping", colour= config.MAIN_COLOR)
		emb.add_field(name= "Bot ping:", value= f"{self.client.ws.latency*1000:.0f} мс")
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	#User
	@commands.command()
	@commands.guild_only()
	async def user(self, ctx):
		emb = discord.Embed(title = f"Информация о {ctx.author.name}", color=config.MAIN_COLOR)
		emb.add_field(name="Ник:",value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
		emb.add_field(name="ID:",value=f"{ctx.author.id}", inline=False)
		emb.set_thumbnail(url=ctx.author.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	#Server
	@commands.command()
	@commands.guild_only()
	async def server(self, ctx):
		emb = discord.Embed(title = f"Информация о сервере **{ctx.guild.name}**", color=config.MAIN_COLOR)
		emb.add_field(name="ID:", value=f"{ctx.guild.id}", inline=False)
		emb.add_field(name="Владелец:", value=f"{ctx.guild.owner}", inline = False)
		emb.set_thumbnail(url=ctx.guild.icon_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	#Hosting
	@commands.command()
	@commands.guild_only()
	async def hosting(self, ctx):

		def bytes2human(number, typer=None):

			if typer == "system":
				symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')
			else:
				symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

			prefix = {}

			for i, s in enumerate(symbols):
				prefix[s] = 1 << (i + 1) * 10

			for s in reversed(symbols):
				if number >= prefix[s]:
					value = float(number) / prefix[s]
					return '%.1f%s' % (value, s)

			return f"{number}B"

		mem = psutil.virtual_memory()



		emb = discord.Embed(title = 'Информация о хостинге', color=config.MAIN_COLOR)
		emb.add_field(name='Хостинг:', value='`TimeWeb`')
		emb.add_field(name='CPU:', value='`1 x 2.8 ГГц`', inline=False)
		emb.add_field(name='RAM:',value=f'`{bytes2human(mem.total, "system")}`',inline=False)
		emb.add_field(name='OS:', value='`Ubuntu 20.04 LTS`', inline=False)
		emb.add_field(name='SSD:', value='`10 GB`')
		emb.set_thumbnail(url=ctx.guild.icon_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)


	#Stats
	@commands.command()
	@commands.guild_only()
	async def stats(self, ctx):

		def bytes2human(number, typer=None):

			if typer == "system":
				symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')
			else:
				symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

			prefix = {}

			for i, s in enumerate(symbols):
				prefix[s] = 1 << (i + 1) * 10

			for s in reversed(symbols):
				if number >= prefix[s]:
					value = float(number) / prefix[s]
					return '%.1f%s' % (value, s)

			return f"{number}B"

		guild_count = len(self.client.guilds)
		all_members = len(set(self.client.get_all_members()))
		mem = psutil.virtual_memory()

		emb = discord.Embed(title = "BorryBot в цифрах", color = config.MAIN_COLOR)
		emb.add_field(name= "Серверов:", value= f"`{guild_count}`",inline=False)
		emb.add_field(name= "Участников:", value= f"`{all_members}`",inline=False)
		emb.add_field(name='RAM:',value=f'`{mem.percent}% / {bytes2human(mem.total, "system")}`',inline=False)
		emb.add_field(name='CPU:',value=f'`{psutil.cpu_percent()}%`',inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)


		
def setup(client):
	client.add_cog(Information(client))
	print('[Cog] Information загружен!')