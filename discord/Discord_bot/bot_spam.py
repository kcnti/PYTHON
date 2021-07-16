import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

client = commands.Bot(command_prefix = '!')

@client.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def r_pung(ctx, member : discord.Member):
    if discord.Member.id == "307448724089733120":
        await ctx.send("Sorry this is my own bot :)")
    else:
        await ctx.send(f"<@{ctx.message.mentions[0].id}>")
        for x in range (0,5):
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
    #await client.leave_server(message.server)


@client.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def pung(ctx, member : discord.Member):

    if discord.Member.id == "307448724089733120":
        await ctx.send("Sorry this is my own bot :)")

    else:
        for x in range (0,4):
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")
            await ctx.send(f"<@{ctx.message.mentions[0].id}>")

stored = "これが"

@client.event
async def on_message(message: discord.Message):
    global stored

    if message.content.startswith("st!echo"):
        await message.delete()

    if message.content.startswith("st!true_echo"):
        await message.delete()

    try:
        id = message.guild.id    #exception raiser
        a = (f"{message.author}: '{message.content}' was sent in {message.guild}")
        print(a)

        stored = 1
    except:
        a = (f"{message.author} directed '{message.content}'")
        stored = 1
        print(a)

    #await channel.send(a)
    await client.process_commands(message)


client.run('NzMxMDQwNDc3OTU2Mjc2MjYz.XwgQgA._SdriDyaRkwLaxHQV-yqTIxQ_CQ')
