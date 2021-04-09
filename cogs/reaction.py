import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Cog

from asyncio import get_event_loop
from sqlite3 import connect

async def _reactroles(r_type, request, save=False):
    connection = connect("./DB/reaction/reaction.db")
    if r_type == 'request' and save:
        connection.cursor().execute(request)
        connection.commit()
    elif r_type == 'request': return connection.cursor().execute(request)
    elif r_type == 'fetchone': return connection.cursor().execute(request).fetchone()
    elif r_type == 'fetchall': return connection.cursor().execute(request).fetchall()

async def create_tables():
    await _reactroles('request', "CREATE TABLE IF NOT EXISTS roles (guild BIGINT, channel BIGINT, message BIGINT, role BIGINT, emoji TEXT)", save=True)
get_event_loop().run_until_complete(create_tables())

class ReactRoles(Cog):
    def __init__(self, bot):
        self.bot = bot

        self.check_emojis.start()
    
    @tasks.loop(minutes=2)
    async def check_emojis(self):
        for item in await _reactroles('fetchall', "SELECT * FROM roles"):
            channel = self.bot.get_channel(item[0])
            if channel:
                message = await channel.fetch_message(item[1])
                role    = channel.guild.get_role(item[2])
                _emojis = []
                for i in message.reactions: _emojis.append(str(i))
                for i in _emojis:
                    if str(i) == item[3] and not role:
                        try: await message.clear_reaction(str(i))
                        except: pass
                        await _reactroles('request', f"DELETE FROM roles WHERE guild = '{item[0]}' AND channel = '{item[1]}' AND message = '{item[2]}' AND role = '{item[3]}'", save=True)
                if item[3] not in _emojis:
                    await _reactroles('request', f"DELETE FROM roles WHERE guild = '{item[0]}' AND channel = '{item[1]}' AND message = '{item[2]}' AND role = '{item[3]}'", save=True)
    
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot: return
        for role_id in await _reactroles('request', f"SELECT role FROM roles WHERE guild = '{payload.guild_id}' AND message = '{payload.message_id}' AND channel = '{payload.channel_id}' AND emoji = '{payload.emoji}'"):
            message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            await message.remove_reaction(payload.emoji, payload.member)
            role = payload.member.guild.get_role(role_id[0])
            if role:
                if role not in payload.member.roles: await payload.member.add_roles(role)
                else: await payload.member.remove_roles(role)
    
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.group(name='react-roles',aliases=['reactroles'])
    async def _react_roles(self, ctx):
        if not ctx.invoked_subcommand:
            return await ctx.send("❌ Неверно указаны аргументы группы:\n" \
                                  "```-react-roles add id-сообщения @role эмодзи - добавить роль по реакциям\n-react-roles remove id-сообщения @role - удалить роль из ролей по реакциям```")
    
    @_react_roles.command(name='add',usage='react-roles add id-сообщения @role эмодзи',description='добавить роль по реакции на сообщение')
    async def _react_roles_add(self, ctx, message_id:int, role:discord.Role, emoji):
        try: message = await ctx.channel.fetch_message(message_id)
        except: return await ctx.send("❌ Данное сообщение с таким ID не найдено в данном канале")
        if str(role) == '@everyone': return await ctx.send("❌ Роль `@everyone` не может быть использована для ролей по реакциям")
        if await _reactroles('fetchone', f"SELECT * FROM roles WHERE guild = '{ctx.guild.id}' AND channel = '{ctx.channel.id}' AND message = '{message_id}' AND role = '{role.id}'"): return await ctx.send("❌ Роль для указанного вами сообщения уже настроенна под одну из реакций")
        elif await _reactroles('fetchone', f"SELECT * FROM roles WHERE guild = '{ctx.guild.id}' AND channel = '{ctx.channel.id}' AND message = '{message_id}' AND emoji = '{emoji}'"): return await ctx.send("❌ Эмодзи для указанного вами сообщения уже настроенна под одну из ролей")
        try: await message.add_reaction(emoji)
        except: return await ctx.send("❌ Не удалось использовать указанную вами реакцию, возможно, что указанное сообщение уже имеет `13 реакций`")
        await _reactroles('request', f"INSERT INTO roles VALUES ({ctx.guild.id}, {ctx.channel.id}, {message.id}, {role.id}, '{emoji}')", save=True)
        await ctx.send(f"✅ Роль `@{role}` успешно установлена для эмодзи {emoji} и прикреплена к сообщению с ID `{message_id}`")
    
    @_react_roles.command(name='remove',usage='react-roles remove id-сообщения @role',description='удалить роль по реакции из сообщения')
    async def _react_roles_remove(self, ctx, message_id:int, role:discord.Role):
        try: message = await ctx.channel.fetch_message(message_id)
        except: return await ctx.send("❌ Данное сообщение с таким ID не найдено в данном канале")
        if str(role) == '@everyone': return await ctx.send("❌ Роль `@everyone` не может быть использована для ролей по реакциям")
        elif not await _reactroles('fetchone', f"SELECT * FROM roles WHERE guild = '{ctx.guild.id}' AND channel = '{ctx.channel.id}' AND message = '{message_id}' AND role = '{role.id}'"):
            return await ctx.send(f"❌ Для данной роли не настроены роли по реакциям для сообщения с ID `{message_id}`")
        for emoji in await _reactroles('request', f"SELECT emoji FROM roles WHERE guild = '{ctx.guild.id}' AND channel = '{ctx.channel.id}' AND message = '{message_id}' AND role = '{role.id}'"): _emoji = emoji[0]
        try: await message.clear_reaction(_emoji)
        except: pass
        await _reactroles('request', f"DELETE FROM roles WHERE guild = '{ctx.guild.id}' AND channel = '{ctx.channel.id}' AND message = '{message_id}' AND role = '{role.id}'", save=True)
        await ctx.send(f"✅ Реакция по роли с эмодзи {_emoji} и ролью `@{role}` была удалена с сообщения с ID `{message_id}`")

def setup(client):
    client.add_cog(ReactRoles(client))
    print('[Cog] ReactRoles загружен!')