import discord
from bot import Bot
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    TOKEN = os.getenv("DISCORD_KEY")

    intents = discord.Intents.default()
    intents.message_content = True

    bot = Bot(command_prefix=".", intents=intents)

    bot.run(str(TOKEN))


if __name__ == "__main__":
    main()