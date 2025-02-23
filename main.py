import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord_bot import start_discord_bot

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Define a simple command
@bot.command()
async def hello(ctx):
	await ctx.send('Hello!')

def main():
    load_dotenv()
    start_discord_bot()

if __name__ == "__main__":
    main()