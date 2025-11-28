import discord 
from discord.ext import commands
import datetime
from config.criacao_ficha import CriarFichaDePersonagem

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @staticmethod
    def criar_embed(title, color, description=None, name1=None, value1=None, name2=None, value2=None):
        embed = discord.Embed(
            title=title,
            description=description,
            color=color,
            timestamp=datetime.datetime.now()
        )

        # Campo 1
        if name1 is not None and value1 is not None:
            embed.add_field(name=name1, value=value1)

        # Campo 2
        if name2 is not None and value2 is not None:
            embed.add_field(name=name2, value=value2)

        return embed

    @commands.command()
    async def teste(self, ctx):
        embed = self.criar_embed(title="Título", description="Descrição", color=discord.Color.random(), name1="Nome", value1="Valor\nValor")
        await ctx.send(embed=embed)

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

        embed = self.criar_embed(
                title="Tem certeza que deseja criar uma ficha de personagem?",
                description="✅ - Sim\n❌ - Não",
                color=discord.Color.yellow()
                )

        msg = await ctx.reply(embed=embed, delete_after=30) # Resposta do Bot
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
        
        # Filtra a seleção do usuário
        if reaction.emoji == "❌": 
            await msg.delete()
            await ctx.send("Criação de ficha cancelada.", delete_after=5)
        else:
            await msg.delete()

        await ctx.send("Iniciando criação de ficha de personagem...", delete_after=5)