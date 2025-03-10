import os

def check_env_variables():
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
        print(f"Missing or invalid values for mandatory environment variables: {', '.join(missing_vars)}")
        update_env_file(missing_vars)
        raise ValueError("Please restart the application after updating the environment variables.")

    # Test the validity of the environment variables
    test_discord_token(os.getenv('DISCORD_TOKEN'))
    test_groq_api_key(os.getenv('GROQ_API_KEY'))
    test_elevenlabs_api_key(os.getenv('ELEVENLABS_API_KEY'), os.getenv('VOICE_ID'))

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
        env_vars[var] = input(f"Please enter the value for {var}: ")

    # Write updated values back to .env file
    with open(env_file_path, 'w') as file:
        for key, value in env_vars.items():
            file.write(f"{key}={value}\n")

def test_discord_token(token):
    # Implement your logic to test the Discord token
    print(f"Testing Discord token: {token}")
    # Example: raise ValueError if the token is invalid
    # raise ValueError("Invalid Discord token")

def test_groq_api_key(api_key):
    # Implement your logic to test the Groq API key
    print(f"Testing Groq API key: {api_key}")
    # Example: raise ValueError if the API key is invalid
    # raise ValueError("Invalid Groq API key")

def test_elevenlabs_api_key(api_key, voice_id):
    # Implement your logic to test the ElevenLabs API key and Voice ID
    print(f"Testing ElevenLabs API key: {api_key} with Voice ID: {voice_id}")
    # Example: raise ValueError if the API key or Voice ID is invalid
    # raise ValueError("Invalid ElevenLabs API key or Voice ID")

if __name__ == "__main__":
    check_env_variables()
    print("All mandatory environment variables are set correctly.")