import discord
from discord.ext import commands

bot = commands.Bot(commnad_prefix='-')

@bot.command()
async def asd(ctx,member,number):
    await ctx.send("<@"+member+">")

bot.run('NzMxMDQwNDc3OTU2Mjc2MjYz.XwgQgA._SdriDyaRkwLaxHQV-yqTIxQ_CQ')