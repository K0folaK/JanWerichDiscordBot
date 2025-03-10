import os
from dotenv import load_dotenv
import conf_check
import logging
import sys
import discord_bot

load_dotenv()
# Nastavení logování
if not os.path.exists('logs'):
    os.makedirs('logs')

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, "logs", "discord_bot.log")

logging.basicConfig(
    filename='d:/vscode/JanWerichDiscordBot/logs/discord_bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    encoding='utf-8'  # Ensure the log file is written with UTF-8 encoding
)

logging.info("Logging has been set up, discord_bot.log path: %s", log_file_path)

# Configure console handler in addition to file handler
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, log_level, logging.INFO))
console_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)


def main():
    """
    Hlavní funkce pro načtení environmentálních proměnných a spuštění Discord bota.
    """
    logging.info("Loading environment variables...")
    logging.info("Environmentální proměnné načteny")

    logging.info("Starting conf_check...")
    try:
        conf_check.check_env_variables()
        logging.info("All mandatory environment variables are set correctly.")
    except ValueError as e:
        logging.error(f"Chyba konfigurace: {e}")
        sys.exit(1)

    logging.info("Starting Discord bot...")
    discord_bot.start_discord_bot()
    logging.info("Discord bot spuštěn")

if __name__ == "__main__":
    main()