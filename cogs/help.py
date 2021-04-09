import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config


prefix = '-'


class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.group()
	async def help(self, ctx):
		if ctx.invoked_subcommand == None:
			emb = discord.Embed(title= "Команды", description = "Для просмотра команд введите `-help <модуль>`" , colour= config.MAIN_COLOR)
			emb.add_field(name= "-help moderation", value= "Команды модерации",inline=False)
			emb.add_field(name= "-help info", value= "Информационные команды",inline=False)
			emb.add_field(name= "-help fun", value= "Развлекательные команды",inline=False)
			emb.add_field(name= "-help settings", value= "Настройки сервера(beta)",inline=False)
			emb.add_field(name= "-help nsfw", value= "NSFW команды",inline=False)
			emb.add_field(name= "-help premium", value= "Премиум команды",inline=False)
			emb.add_field(name= "-help utility", value= "Полезные команды",inline=False)
			emb.add_field(name= "-help support", value= "Команды поддержки",inline=False)
			emb.set_thumbnail(url=self.client.user.avatar_url)
			emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
			await ctx.send(embed = emb)
			

	@help.command()
	async def moderation(self, ctx):
		emb = discord.Embed(title= "Команды модерации", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-ban <пинг участника> [причина]`", value= "Забанить участника на сервере",inline=False)
		emb.add_field(name= "`-clear [кол-во сообщений(макс. 50)]`", value= "Очистить определённое кол-во сообщений",inline=False)
		emb.add_field(name= "`-kick <пинг участника> [причина]`", value= "Выгнать участника с сервера",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def info(self, ctx):
		emb = discord.Embed(title= "Информационные команды", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-info`", value= "Узнать информацию о боте",inline=False)
		emb.add_field(name= "`-ping`", value= "Узнать пинг бота",inline=False)
		emb.add_field(name= "`-stats`", value= "BorryBot в цифрах",inline=False)
		emb.add_field(name= "`-hosting`", value= "Узнать информацию о хостинге", inline=False)
		emb.add_field(name= "`-server`", value= "Узнать информацию о сервере", inline=False)
		emb.add_field(name= "`-user`", value= "Узнать ниформацию о пользователе",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def fun(self, ctx):
		emb = discord.Embed(title= "Развлекательные команды", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-bird`", value= "Рандомное фото птицы",inline=False)
		emb.add_field(name= "`-cat`", value= "Рандомное фото кота",inline=False)
		emb.add_field(name= "`-dog`", value= "Рандомное фото собаки",inline=False)
		emb.add_field(name= "`-fox`", value= "Рандомное фото лисы",inline=False)
		emb.add_field(name= "`-koala`", value= "Рандомное фото коалы",inline=False)
		emb.add_field(name= "`-panda`", value= "Рандомное фото панды",inline=False)
		emb.add_field(name= "`-dice`", value= "Бросить кость",inline=False)
		emb.add_field(name= "`-eightball [вопрос]`", value= "Задать вопрос шару предсказаний",inline=False)
		emb.add_field(name= "`-hug <пинг участника>`", value= "Обнять участника сервера",inline=False)
		emb.add_field(name= "`-wink <пинг участника>`", value= "Подмингнуть участнику сервера",inline=False)
		emb.add_field(name= "`-pat <пинг участника>`", value= "Погладить участника сервера",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def settings(self, ctx):
		emb = discord.Embed(title= "Настройки сервера(beta)", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-add-role <ID роли/пинг роли>`", value= "Добавить авто-роль",inline=False)
		emb.add_field(name= "`-remove-role <ID роли/пинг роли>`", value= "Удалить авто-роль",inline=False)
		emb.add_field(name= "`-react-roles add <ID сообщения> <пинг роли> [эмодзи]`", value= "Добавить роль по реакции",inline=False)
		emb.add_field(name= "`-remove-role <ID роли/пинг роли>`", value= "Удалить роль по реакции",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	@commands.is_nsfw()
	async def nsfw(self, ctx):
		emb = discord.Embed(title= "NSFW команды", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-cum`", value= "Сперма",inline=False)
		emb.add_field(name= "`-anal`", value= "Анал",inline=False)
		emb.add_field(name= "`-tits`", value= "Грудь",inline=False)
		emb.add_field(name= "`-pussy`", value= "Киска",inline=False)
		emb.add_field(name= "`-nsfw_random`", value= "Рандомная гифка",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def utility(self, ctx):
		emb = discord.Embed(title= "Полезные команды", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-calc [пример]`", value= "Посчитать математический пример",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def premium(self, ctx):
		emb = discord.Embed(title= "Премиум команды", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-donate`", value= "Оформить премиум подписку",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def support(self, ctx):
		emb = discord.Embed(title= "Команды поддержки", colour= config.MAIN_COLOR)
		emb.add_field(name= "`-bug [суть бага]`", value= "Отправить баг владельцу бота",inline=False)
		emb.add_field(name= "`-idea` [суть идеи]", value= "Отправить идею владельцу бота")
		emb.add_field(name= "`-invite`", value= "Добавить бота на свой сервер",inline=False)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
		await ctx.send(embed = emb)

	@help.command()
	async def admin(self, ctx):
		if ctx.author.id == 707850121814999090:
			emb = discord.Embed(title= "Команды владельца", colour= config.MAIN_COLOR)
			emb.add_field(name= "`-aban <ID пользователя>`", value= "Добавить пользователя в ЧС бота",inline=False)
			emb.add_field(name= "`-aunban <ID пользователя>`", value= "Удалить пользователя из ЧС бота",inline=False)
			emb.add_field(name= "`-reload <модуль>`", value= "Перезагрузить модуль",inline=False)
			emb.set_thumbnail(url=self.client.user.avatar_url)
			emb.set_footer(text = f'{self.client.user.name} © 2021 | Все права защищены', icon_url = self.client.user.avatar_url)
			await ctx.send(embed = emb)
		else:
			await ctx.send(embed=discord.Embed(title= "Нет доступа!", description=f"Данная команда доступна только основателю бота!", colour= config.ERR_COLOR))




def setup(client):
	client.add_cog(Help(client))
	print('[Cog] Help загружен!')