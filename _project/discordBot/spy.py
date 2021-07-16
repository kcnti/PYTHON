import random
import string
import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
	print(f'logged in as {bot.user}')

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
async def tri(ctx,number,time,threads,counts):
	phone = str(number)
	count = counts
	if target[0] == "0":
		target = "66" + target[1:]
	if (phone == "66955020092"):
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {phone} with {count} times")
		os.system(f"timeout 10s js Abuse.js {phone} {count}")

@bot.command()
async def abuse2(ctx,number,counts):
	phone = number
	count = counts
	if target[0] == "0":
		target = "66" + target[1:]
	if (phone == "66955020092"):
       		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {phone} with {count} times")
		os.system(f"timeout 10s js Abuse.js {phone} {count}")

@bot.command()
async def sms2(ctx,number,time,threads):
	target = number
	timeout = time
	threads = threads
	if target[0] == "0":
		target = "66" + target[1:]
	if target == 66955020092:
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {target} {threads} threads {timeout} seconds")
		os.system(f"timeout {timeout}s quack --target {target} --tool SMS --timeout {timeout} --threads {threads}")
		await asyncio.sleep(timeout)
		await ctx.send("> quack Finished")

@bot.command()
@commands.has_role('spam permission')
async def s_sms2(ctx,number,loop):
	phone = str(number)
	loop = loop
	if target[0] == "0":
		target = "66" + target[1:]
	if phone == "66955020092":
		await ctx.send("???")
	else:
		await ctx.send(f"> Start sending SMS to {phone} with {loop} loops")
		os.system(f"python3 smss.py {phone} {loop}")


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

bot.run('NzM3NjAyNDY4MzM4NDY2ODE2.Xx_v1A.3PQ_5kbIaOkAGR7BQC4ZM4fWzEk')
