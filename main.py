import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord_bot import start_discord_bot

# Create a new bot instance
intents = discord.Intents.default()
bot = commands.Bot(intents=intents)

def main():
    load_dotenv()
    start_discord_bot()

if __name__ == "__main__":
    main()