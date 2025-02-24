import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
import io
from openai_api import generate_text

# Load the .env file
load_dotenv()

def synthesize_speech(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("VOICE_ID")

    elevenlabs = ElevenLabs(api_key=api_key)
    audio_generator = elevenlabs.generate(
        text=text,
        voice=voice_id
    )
    audio_data = io.BytesIO()
    for chunk in audio_generator:
        audio_data.write(chunk)
    audio_data.seek(0)  # Reset the pointer to the beginning of the BytesIO object
    return audio_data

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    text = generate_text(prompt)
    print(f"Generated text: {text}")
    audio_data = synthesize_speech(text)
    # You can now use audio_data as needed without saving to a file
    # For example, you can play it directly or send it over a network