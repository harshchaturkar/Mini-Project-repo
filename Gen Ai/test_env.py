from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
mistral_key = os.getenv("MISTRAL_API_KEY")

if groq_key and mistral_key:
    print("API keys loaded successfully!")
else:
    print("API keys are missing.")