import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging
from discord_bot import start_discord_bot
import conf_check

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
    try:
        conf_check.check_env_variables()  # Check environment variables
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        print(f"Configuration error: {e}")
        return

    load_dotenv()  # Load environment variables from .env file
    logging.info("Environment variables loaded")
    start_discord_bot()  # Start the Discord bot
    logging.info("Discord bot started")

if __name__ == "__main__":
    main()