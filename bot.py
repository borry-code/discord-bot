import discord
from discord.ext import commands
import os

import config

prefix = '-'
client = commands.Bot(command_prefix = prefix, intents=discord.Intents.all())

client.remove_command("help")

@client.command()
async def reload(ctx, extension=None):
	if ctx.author.id == config.DEVELOPERS:
		if extension == None:
			await ctx.send(embed=discord.Embed(title= "Не указан модуль!", description=f"Укажите модуль для его перезагрузки!", colour= 0xff0000))
		else:
			client.unload_extension(f"cogs.{extension}")
			client.load_extension(f"cogs.{extension}")
			await ctx.send(embed=discord.Embed(title= f"Модуль {extension} перезагружен!", colour= 0x6495ed))
	else:
		await ctx.send(embed=discord.Embed(title= "Нет доступа!", description=f"Данная команда доступна только основателю бота!", colour= 0xff0000))




for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(config.TOKEN)

