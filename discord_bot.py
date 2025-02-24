import os
import discord
import logging
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')

# Get the logging level from the .env file, default to INFO if not set
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    filename='logs/discord_bot.log',
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s'
)

def start_discord_bot():
    token = os.getenv("DISCORD_TOKEN")
    client = discord.Client()

    @client.event
    async def on_ready():
        logging.info(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        logging.info(f"Message from {message.author}: {message.content}")
        if "warning" in message.content.lower():
            logging.warning(f"Warning message from {message.author}: {message.content}")
        if "error" in message.content.lower():
            logging.error(f"Error message from {message.author}: {message.content}")

    client.run(token)