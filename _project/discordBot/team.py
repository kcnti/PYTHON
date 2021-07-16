import discord
from discord.ext import commands
import sys

bot = commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    channel = bot.get_channel(808709744394633226)
    mes = "<@&808713628517269504> เริ่มเรียนแล้วพวกโง่"
    await channel.send(mes)
    sys.exit()

"""@bot.event
async def on_message(message):
    channel = bot.get_channel(808709744394633226)
    mes = "@Deklian เริ่มเรียนแล้วพวกโง่"
    await channel.send(mes)
    """

bot.run('ODA4NzExNDg3NjIyMzQ4ODYx.YCKhQw.3LT2JSKrdE1S9VGdEgFcOiXeTNo')