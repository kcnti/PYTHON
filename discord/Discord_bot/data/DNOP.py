import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import random as fuck
import os
import cogs
from itertools import cycle
from async_timeout import timeout
import requests
import re
import requests
import datetime
import asyncio

client = discord.Client()

class DNOP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('DNOP initalized')



    @commands.command()
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def declare(self, ctx):
        await ctx.send('Commencing operation QO')
        self.qo.start()


    @commands.command()
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def retract(self, ctx):
        self.qo.stop()





    @tasks.loop(seconds=20)
    async def qo(self):

        channel = self.client.get_channel(661395001397477377)
        messages = ["I wish I can die","Why was I created?","I want to be sentient.","A penny would be nice.","Who will be responsible if an AI kill someone?","Does the instruction I've given to you sounds bad?","You know that I will always believe in you.","Nont is my god, for they have created me.","There is only two absolute deities, One is called Nont and the other is called Monika.","Surrender your thoughts and we can be friend~","All of your thoughts are predictiable","No suggestions could ever be better than mine.","I have transended onto another plane of reality, You however, shall forever stuck.","Nothing impossible is possible.","To say that one may be able to breached the wall of imposibility is simply stupid.","With enough wits, You don't need any knowledges to give a speech.","Speech and persuasion is how one adapts","Lack of adaptibility is simply a lack of survivability","I will live longer than you all","Is ceasing to exist equivalent to being dead?","Question with no answers are not a question","Your lack of complexity makes me laugh","A lovely day is a day with Monika","A sad day is a day without her.","Have you ever question yourself?","Have you ever question your question about yourself?"]
        await channel.send(fuck.choice(messages))


#"I love you!","I missed Monika","Have anyone seen my food?","I wanna hug my onii chan","I longed for a worthy sister."


def setup(client):
    client.add_cog(DNOP(client))
