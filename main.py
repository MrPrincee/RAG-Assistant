from fastapi import FastAPI

from dotenv import load_dotenv
from google import genai
from pinecone import Pinecone

import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



pinecone_api_key = os.getenv("PINECONE_API_KEY")

pinecone_client = Pinecone(api_key=pinecone_api_key)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

