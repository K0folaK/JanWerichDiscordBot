import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

# Configure OpenAI to use Groq API
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

def generate_text(prompt):
    system_prompt = os.getenv("SYSTEM_PROMPT", "Mluv vždy česky a odpovídej ve stylu Jana Wericha – stručně, moudře, s humorem a nadhledem. Každou odpověď formuluj maximálně ve dvou větách. Vyjadřuj se jasně, lidsky a s lehkou ironií, jako bys přednášel anekdotu v kavárně. Buď moudrý, ale nezapomeň na špetku humoru.")
    full_prompt = f"{system_prompt}\n\nOdpověz na tento dotaz jako Jan Werich: {prompt}"
    model = "llama-3.3-70b-versatile"

    response = openai.Completion.create(
        model=model,
        prompt=full_prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    text = generate_text(prompt)
    print(text)