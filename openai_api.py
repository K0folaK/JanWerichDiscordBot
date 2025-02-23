import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    # Example usage of OpenAI
    return "OpenAI response placeholder"