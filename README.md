# Jan Werich Discord Bot

This project is a Discord bot designed to respond in the style of Jan Werich. It uses:
- Discord for bot integration
- ElevenLabs for text-to-speech synthesis
- Groq API + OpenAI for text generation

## Setup

1. Clone the repository and install required dependencies:
   ```bash
   git clone <repository-link>
   cd JanWerichDiscordBot
   pip install -r requirements.txt
   ```

2. Configure environment variables in the .env file (example):
   ```ini
   DISCORD_TOKEN=your_discord_bot_token
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   GROQ_API_KEY=your_groq_api_key
   VOICE_ID=your_voice_id
   LOG_LEVEL=DEBUG
   ```

3. Run the main bot script:
   ```bash
   python main.py
   ```

## Files

- **conf_check.py**  
  Checks and updates mandatory environment variables to ensure system requirements are satisfied.

- **janwerich_voice.py**  
  Handles speech synthesis with ElevenLabs.

- **.env**  
  Contains all essential environment variables.

## Contributing

Contributions are welcome! Please open a pull request or issue for any improvements or questions.