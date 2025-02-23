# JanWerichDiscordBot

This repository contains a Discord bot that integrates with ElevenLabs and OpenAI APIs.

## Features

- Generates responses using OpenAI API
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

4. Create a [.env](http://_vscodecontentref_/1) file and add your API keys:
    ```env
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

5. Run the bot:
    ```sh
    python main.py
    ```

## Files

- [discord_bot.py](http://_vscodecontentref_/2): Contains the main logic for the Discord bot.
- [elevenlabs.py](http://_vscodecontentref_/3): Contains the function to synthesize speech using ElevenLabs API.
- [main.py](http://_vscodecontentref_/4): Entry point of the application.
- [openai_api.py](http://_vscodecontentref_/5): Contains the function to get responses from OpenAI API.

## License

This project is licensed under the MIT License.