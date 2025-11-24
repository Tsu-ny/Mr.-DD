import discord
from discord.ext import commands
import random

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def d20(self, ctx):
        roll = random.randint(1, 20)
        await ctx.reply(f'`{roll}`')



    @commands.command()
    async def ping(self, ctx):
        await ctx.reply('Pong!')