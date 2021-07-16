import discord
from discord.ext import commands
import os
import random
import csv
import inspect
import asyncio
import functools
import math


class rp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Rp event chain actualized.')

    @commands.command()
    #@commands.cooldown(1, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, commands.BucketType.user)
    async def profile_gen(self, ctx):

        random.seed(ctx.message.author)
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 100)
        num4 = random.randint(0, 100)

        await ctx.send(f'Greetings to {ctx.message.author}')
        await ctx.send(f'Initial stability: {num1}')
        await ctx.send(f'Initial subject loyality: {num2}')
        await ctx.send(f'Initial political power: {num3}')
        await ctx.send(f'Initial financial standing: {num4}')
        #await ctx.send(f'Estimated diplomatic value: {num3*2+num1+num4}')


        with open('./data/data.csv' , 'a+' , newline='' , encoding = 'utf8') as ff:
            wr = csv.writer(ff)
            author = str(ctx.message.author.id)
            print(author)

            wr.writerow([f'"{author}"',num1,num2,num3,num4])


        if num1+num2+num3+num4 <= 100:
            await ctx.send(f'The result is quite pathethic. Please contact the coder for aid.')

        else:
            await ctx.send(f'Data Finalized. Please do not use this command ever again.')


    @commands.command(pass_context = True)
    async def stat(self, ctx):
        Flag = True
        with open('./data/data.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(ctx.message.mentions[0].id) in str(row[0]):
                    await ctx.send(f'{ctx.message.mentions[0]} stats are as follows:\nStability: {float(row[1])}\nSubject Loyality: {float(row[2])}\nPolitical Power: {float(row[3])}\nFinancial Standing: {float(row[4])}')
                    Flag = False

            if Flag == True:
                await ctx.send("User not found.")
                print('asdakjsflkajsflkajfck;;')







    @commands.command()
    async def global_stat(self,ctx):
        await ctx.send('Retriving global stat.')

        with open('./data/data.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                await ctx.send(row)

                #await ctx.send(f'User ID: {float(row[0])}\nStability: {float(row[1])}\nSubject Loyality: {float(row[2])}\nPolitical Power: {float(row[3])}\nFinancial Standing: {float(row[4])}')




    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def address(self, ctx ,):
        await ctx.send('')









'''

        with open('./data/data.csv') as Ass:
            reader = css.reader(Ass)
            for row in reader:
                print(row['User ID'], row['ST'], row['LO'],row['PO'],row['FI'])

'''







                #    break
        #await ctx.send('Unregistered or broken')







    #@profile_gen.error
    #async def profgen_error(self, ctx, error):
    #    if isinstance(error, commands.CommandOnCooldown):
    #        msg = 'You have already registered'
    #        await ctx.send(msg)
    #    else:
    #        raise error









def setup(client):
    client.add_cog(rp(client))
