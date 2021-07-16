import discord
from discord.ext import commands
import asyncio
from google_speech import Speech

bot = commands.Bot(command_prefix = ';')
allowedID = [279970880610893833]

@bot.event
async def on_ready():
	print(f'logged in as {bot.user}')
	state = "ตัวแทนพี่เอิร์ธ"
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(state))

@bot.command()
async def join(ctx):
	vc = await ctx.author.voice.channel.connect()
	lang = input('lang: ')
	while True:
		text = input('text: ')
		if text == "!c":
			lang = input('lang: ')
		speech = Speech(text, lang)
		speech.save("output.mp3")
		user = ctx.message.author
		voice_channel = user.voice.channel
		channel = None
		if voice_channel != None:
			vc.play(discord.FFmpegPCMAudio(f'./output.mp3'))
			while vc.is_playing():
				await asyncio.sleep(1)

@bot.command()
async def dc(ctx):
	await ctx.voice_client.disconnect()

bot.run('NzM3NjAwOTM1NjU5OTYyMzY4.Xx_uZw.iOQK5ASeiGNezmbXrPIkclU9xZw')
