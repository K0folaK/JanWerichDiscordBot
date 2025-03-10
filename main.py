import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging
from discord_bot import start_discord_bot
import conf_check
from conf_check import check_env_variables
import sys

# Nastavení logování
if not os.path.exists('logs'):
    os.makedirs('logs')

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, "logs", "main.log")

logging.basicConfig(
    filename=log_file_path,
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s'
)

logging.info("Logging has been set up, main.log path: %s", log_file_path)

# Configure console handler in addition to file handler
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, log_level, logging.INFO))
console_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# Vytvoření nové instance bota s výchozími intenty
intents = discord.Intents.default()
bot = commands.Bot(intents=intents)

def main():
    """
    Hlavní funkce pro načtení environmentálních proměnných a spuštění Discord bota.
    """
    start_discord_bot()
    logging.info("Discord bot spuštěn")

if __name__ == "__main__":
    logging.info("Loading environment variables...")
    load_dotenv()
    logging.info("Environmentální proměnné načteny")

    logging.info("Starting conf_check...")
    try:
        conf_check.check_env_variables()
        logging.info("All mandatory environment variables are set correctly.")
    except ValueError as e:
        logging.error(f"Chyba konfigurace: {e}")
        raise SystemExit(1)

    main()