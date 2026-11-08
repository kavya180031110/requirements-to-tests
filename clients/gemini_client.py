import os
from dotenv import load_dotenv
from google import genai

#Load the environment variables from the .env file
load_dotenv()
key = os.getenv("GEMINI_API_KEY")

if not key:
    raise ValueError("GEMINI_API_KEY missing. Copy .env.example to .env and add your key.")

# Initialize the Gemini client with the API key
client = genai.Client(api_key=key)

# Generate response by sending the prompt to AI client
def generate_response(prompt):
    response = client.models.generate_content(model = "gemini-3.5-flash-lite", contents = prompt)
    return response.text