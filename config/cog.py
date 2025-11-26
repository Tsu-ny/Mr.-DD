import discord 
from discord.ext import commands
import asyncio
from config.criacao_ficha import CriarFichaDePersonagem

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.reply('Pong!')
        await msg.add_reaction('🏓')

    @commands.command()
    async def ficha(self, ctx):
        '''
        Criação de ficha de personagem para RPGs.

        Cria um embed perguntando se o usuário tem certeza que deseja criar uma ficha de personagem.
        '''

        embed = discord.Embed(
            title="Tem certeza que deseja criar uma ficha de personagem?",
            description="✅ para Sim\n"
            "❌ para Não",
            color=discord.Color.yellow()
        )


        msg = await ctx.reply(embed=embed)
        options = ["✅", "❌"] # ✅ | ❌
            
        for emoji in options:
            await msg.add_reaction(emoji) # Seleciona as reações

        def checkup(reaction, user):
            '''
            Verifica se a reação é válida.
            '''
            return (
                user == ctx.author and 
                reaction.emoji in options and 
                reaction.message.id == msg.id
            )
           
        reaction, user = await self.bot.wait_for('reaction_add', check=checkup) # Espera pela reação do usuário
        

        if reaction.emoji == "❌": # Filtra a seleção do usuário
            await msg.delete()
            await ctx.send("Criação de ficha cancelada.")
            return
        else:
            await msg.delete()

        await ctx.send("Iniciando criação de ficha de personagem...")
        # questions = {
        #     "nome": "Qual nome vai definir para o seu personagem?",
        #     "classe": "Qual classe ele terá?"
        # }

        # answers = {}

        # for key, question in questions.items():
        #     await ctx.send(question)

        #     def check(m):
        #         return m.author == ctx.author and m.channel == ctx.channel

        #     try:
        #         msg = await self.bot.wait_for('message', check=check, timeout=60)
        #     except asyncio.TimeoutError:
        #         await ctx.send("Tempo esgotado! Por favor, tente novamente.")
        #         return
        #     else:
        #         answers[key] = msg.content