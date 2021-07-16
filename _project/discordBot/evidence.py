import discord
import os
from discord.ext import commands
import mysql.connector
import asyncio
from base64 import b64encode
import subprocess

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
	print(f'logged in as {bot.user}')
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("ขอทางหน่อยค้าบ"))

@bot.event
async def on_message(message: discord.Message):
	try:
		mes = (f"{message.author}: '{message.content}' was sent in server {message.guild} in channel {message.channel.name}")
		print(mes)
		user = bot.get_user(279970880610893833)
		await user.send(mes)
		#channel = bot.get_channel(769436332468338728)
		#await channel.send(mes)
	except:
		mes = (f"{message.author} directed '{message.content}'")
		print(mes)
		#raise

@commands.Cog.listener()
async def on_message_delete(self, c):
	if(c.guild):
		if c.guild.name == "BotHia":
			channel = bot.get_channel(769436332468338728)
			if c.author.bot == True:
				mes = (f"Bot: {c.author} deleted --- {c.clean_content} --- in #{c.channel.name}")
				await channel.send(mes)
			else:
				mes = (f"User: {c.author} deleted --- {c.clean_content} --- in #{c.channel.name}")
				await channel.send(mes)

bot.run('NzU0NjI5ODk1MTc4NTUxMzk2.X13h2w.rqqnTLYiSVhxhF-jTmQX2ZiTxgc')