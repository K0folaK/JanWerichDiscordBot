import os
import logging
from dotenv import load_dotenv
import requests
import openai

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')

# Get the logging level from the .env file, default to INFO if not set
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    filename='logs/conf_check.log',
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

def check_env_variables():
    logging.info("Starting check_env_variables function")
    """
    Checks if mandatory environment variables are set or not equal to placeholders.
    Raises a ValueError if any variables are missing or invalid.
    """
    load_dotenv()  # Load environment variables from .env file

    mandatory_vars = {
        'DISCORD_TOKEN': 'YOUR_DISCORD_BOT_TOKEN',
        'ELEVENLABS_API_KEY': 'YOUR_ELEVENLABS_API_KEY',
        'GROQ_API_KEY': 'YOUR_GROQ_API_KEY',
        'VOICE_ID': 'YOUR_VOICE_ID'
    }

    missing_vars = []
    for var, placeholder in mandatory_vars.items():
        value = os.getenv(var)
        if not value or value == placeholder:
            missing_vars.append(var)

    if missing_vars:
        logging.error(f"Missing or invalid values for mandatory environment variables: {', '.join(missing_vars)}")
        update_env_file(missing_vars)
        raise ValueError("Please restart the application after updating the environment variables.")

    # Test the validity of environment variables
    try:
        test_discord_token(os.getenv('DISCORD_TOKEN'))
    except ValueError as e:
        update_env_file(['DISCORD_TOKEN'])
        load_dotenv()  # Load environment variables
        logging.error(f"Error: {e}")
        return

    try:
        test_groq_api_key(os.getenv('GROQ_API_KEY'))
    except ValueError as e:
        update_env_file(['GROQ_API_KEY'])
        load_dotenv()  # Load environment variables
        logging.error(f"Error: {e}")
        return

    try:
        test_elevenlabs_api_key(os.getenv('ELEVENLABS_API_KEY'), os.getenv('VOICE_ID'))
    except ValueError as e:
        if str(e) == "Invalid ElevenLabs Voice ID":
            update_env_file(['VOICE_ID'])
        else:
            update_env_file(['ELEVENLABS_API_KEY'])
        load_dotenv()  # Load environment variables
        logging.error(f"Error: {e}")
        return

def update_env_file(missing_vars):
    env_file_path = '.env'
    env_vars = {}

    # Read existing .env file
    if os.path.exists(env_file_path):
        with open(env_file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value

    # Prompt user for missing variables
    for var in missing_vars:
        env_vars[var] = input(f"Please enter a value for {var}: ")

    # Write updated values back to .env file
    with open(env_file_path, 'w') as file:
        for key, value in env_vars.items():
            file.write(f"{key}={value}\n")

    load_dotenv()  # Load environment variables after updating the file

def test_discord_token(token):
    """
    Tests the validity of the provided Discord token.
    """
    url = "https://discord.com/api/v10/users/@me"
    headers = {"Authorization": f"Bot {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logging.info("Testing Discord token: OK")
    else:
        raise ValueError("Invalid Discord token")

def test_groq_api_key(api_key):
    """
    Tests the Groq API key by attempting a sample completion.
    """
    openai.api_key = api_key
    openai.api_base = "https://api.groq.com/openai/v1"
    system_prompt = os.getenv("SYSTEM_PROMPT", "Speak in the style of Jan Werich – briefly, wisely, with humor and perspective. Formulate each answer in no more than two sentences.")
    try:
        openai.ChatCompletion.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Test API key"}
            ],
            max_tokens=1
        )
        logging.info("Testing Groq API key: OK")
    except Exception:
        raise ValueError("Invalid Groq API key")

def test_elevenlabs_api_key(api_key, voice_id):
    """
    Tests the ElevenLabs API key and Voice ID by requesting voice data.
    """
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        logging.info("Testing ElevenLabs API key: OK")
        voices_data = response.json()
        voice_ids = [voice.get("voice_id", "") for voice in voices_data.get("voices", [])]
        if voice_id in voice_ids:
            logging.info("Testing ElevenLabs Voice ID: OK")
        else:
            raise ValueError("Invalid ElevenLabs Voice ID")
    else:
        raise ValueError("Invalid ElevenLabs API key")

if __name__ == "__main__":
    try:
        check_env_variables()
        logging.info("All mandatory environment variables are set correctly.")
    except ValueError as e:
        logging.error(f"Error: {e}")