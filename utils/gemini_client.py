from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    return client