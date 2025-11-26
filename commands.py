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

    # @commands.command()
    # async def registro(self, ctx):
    #     """Para criar um registro de personagem para RPGs."""
    #     embed = discord.Embed(
    #         title="Registro de Personagem",
    #         description=(
    #             "Use o comando abaixo para criar um registro de personagem para RPGs.\n\n"
    #             "`!criar_personagem Nome Idade Classe Raça`"
    #         ),
    #         color=discord.Color.blue()
    #     )
    #     await ctx.reply(embed=embed)