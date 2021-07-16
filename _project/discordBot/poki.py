import random
import string
import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix = ';')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.command()
async def dm(ctx, member : discord.Member, message, loop):
    for i in range(int(loop)):
        user = bot.get_user(int(ctx.message.mentions[0].id))
        await user.send(message)

@bot.command()
async def loopconn(ctx, loop):
    _loop = int(loop)
    conn = ctx.author.voice.channel
    for i in range(_loop):
        await conn.connect()
        #asyncio.sleep(0.5)
        await ctx.voice_client.disconnect()


@bot.command()
@commands.has_role('spam permission')
async def tri(ctx,number,time,threads,counts,loop):
	target = str(number)
	loop = loop
	if target[0] == "0":
		target = "66" + target[1:]
	if target == "66955020092":
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {target} with {loop} loops")
		os.system(f"python3 smss.py {target} {loop}")

@bot.command()
@commands.has_role('spam permission')
async def abuse3(ctx,number,counts):
	phone = number
	count = counts
	if (phone == "66955020092"):
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {phone} with {count} times")
		os.system(f"timeout 10s js Abuse.js {phone} {count}")

@bot.command()
@commands.has_role('spam permission')
async def sms3(ctx,number,time,threads):
    target = str(number)
    timeout = time
    threads = threads
    if target[0] == "0":
       target = "66" + target[1:]
    if target == "66955020092":
        await ctx.send("???")
    else:
        await ctx.send(f"> Start sending SMS to {target} {threads} threads {timeout} seconds.\n(Wait for {timeout} seconds then you can attack again.)")
        os.system(f"timeout {timeout}s quack --target {target} --tool SMS --timeout {timeout} --threads {threads}")
        await asyncio.sleep(timeout)
        await ctx.send('quack Finished')

@bot.command()
@commands.has_role('spam permission')
async def s_sms3(ctx,number,loop):
    phone = str(number)
    loop = loop
    if target[0] == "0":
        target = "66" + target[1:]
    if phone == "66955020092":
        await ctx.send("???")
    else:
        await ctx.send(f"> Start sending SMS to {phone} with {loop} loops")
        os.system(f"python3 smss.py {phone} {loop}")

bot.run('NzM3NjAwOTM1NjU5OTYyMzY4.Xx_uZw.iOQK5ASeiGNezmbXrPIkclU9xZw')
