import discord
from discord.ext import commands
from config.cog import Cogs


class Bot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Bot online como {self.user}')

        # Define a presença do bot
        await self.change_presence(activity=discord.Game(name=""))
        await self.change_presence(status=discord.Status.online)

    async def setup_hook(self):
        # Adiciona os Cogs ao bot
        await self.add_cog(Cogs(self))
