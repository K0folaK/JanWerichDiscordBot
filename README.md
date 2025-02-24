# JanWerichDiscordBot

This repository contains a Discord bot that integrates with ElevenLabs and Groq APIs.

## Features

- Generates responses using Groq API
- Synthesizes speech using ElevenLabs API

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/JanWerichDiscordBot.git
    cd JanWerichDiscordBot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following variables:
    ```properties
    # Discord bot token
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN

    # ElevenLabs API key
    ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY

    # Groq API key
    GROQ_API_KEY=YOUR_GROQ_API_KEY

    # ElevenLabs Voice ID
    VOICE_ID=YOUR_VOICE_ID  # Jan Werich voice

    # Logging level
    LOG_LEVEL=DEBUG
    ```

    Replace the placeholder values with your actual keys and IDs.

5. Run the bot:
    ```sh
    python main.py
    ```

## Files

- [discord_bot.py](http://_vscodecontentref_/2): Contains the main logic for the Discord bot.
- [elevenlabs.py](http://_vscodecontentref_/3): Contains the function to synthesize speech using ElevenLabs API.
- [main.py](http://_vscodecontentref_/4): Entry point of the application.
- [openai_api.py](http://_vscodecontentref_/5): Contains the function to get responses from OpenAI API.

## API Usage

This bot uses the Groq API instead of the OpenAI API for its functionalities. Make sure to provide the correct Groq API key in the `.env` file.

## License

This project is licensed under the MIT License.