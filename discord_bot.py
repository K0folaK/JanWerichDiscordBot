import os
import discord
import logging
from dotenv import load_dotenv
from groq_text_api import generate_text
from janwerich_voice import synthesize_speech
from datetime import datetime

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
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    logging.info(f"Received message from {message.author}: {message.content}")
    if message.author == client.user:
        return

    prefixes = ["Janku,", "Jane,", "Pane Werich,"]
    for prefix in prefixes:
        if message.content.startswith(prefix):
            prompt = message.content[len(prefix):].strip()
            logging.info(f"Received prompt: {prompt}")

            # Generate text using Groq API
            generated_text = generate_text(prompt)
            logging.info(f"Generated text: {generated_text}")

            # Synthesize speech using ElevenLabs
            audio_data = synthesize_speech(generated_text)

            # Send the generated text back to the Discord channel
            # await message.channel.send(f"{generated_text}")

            # Optionally, you can send the audio file back to the Discord channel
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            audio_filename = f"JanWerich_{timestamp}.wav"
            with open(audio_filename, "wb") as f:
                f.write(audio_data.getbuffer())
            await message.channel.send(file=discord.File(audio_filename))
            break

client.run(os.getenv("DISCORD_TOKEN"))