import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

def generate_text(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    text = generate_text(prompt)
    print(text)