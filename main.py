import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging
from discord_bot import start_discord_bot

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    filename='logs/main.log',
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s'
)

# Create a new bot instance with default intents
intents = discord.Intents.default()
bot = commands.Bot(intents=intents)

def main():
    """
    Main function to load environment variables and start the Discord bot.
    """
    load_dotenv()  # Load environment variables from .env file
    logging.info("Environment variables loaded")
    start_discord_bot()  # Start the Discord bot
    logging.info("Discord bot started")

if __name__ == "__main__":
    main()