import discord
from discord.ext import commands,tasks
import os


class Sel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Sel event chain loaded.')

    #@commands.Cog.listener()
    #async def on_ready2(ctx):
    #    ctx.send('Tremble before me fools, I am GO-')
    #    ctx.send('Bot loaded.')

    @commands.command()
    async def sele(self, ctx):
        await ctx.send('Sel event chain loaded successfully.')




def setup(client):
    client.add_cog(Sel(client))
