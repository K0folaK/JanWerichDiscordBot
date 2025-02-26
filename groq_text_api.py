import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

# Configure OpenAI to use Groq API
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

def generate_text(prompt):
    system_prompt = os.getenv("SYSTEM_PROMPT", "Respond in the style of Jan Werich – concisely, wisely, with humor and perspective. Formulate each answer in no more than two or thre sentences. Express yourself clearly, humanly, and with a touch of irony, as if you were telling an anecdote in a café. Be wise, but don’t forget a pinch of humor.")
    full_prompt = f"{system_prompt}\n\nRespond to this query as Jan Werich: {prompt}"
    model = "llama-3.3-70b-versatile"

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message['content'].strip()

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    text = generate_text(prompt)
    print(text)