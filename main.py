from fastapi import FastAPI

from utils.pdf_reader import pdf_reader
from utils.create_index import create_index
from utils.gemini_client import get_gemini_client
from utils.text_splitter import text_splitter
from utils.embeddings import embedding_model
from google.genai import types


#Gemini API client
gemini_client = get_gemini_client()


#extract text from PDF
full_text = pdf_reader("fruits.pdf")


chunks = text_splitter(full_text)


embeddings = embedding_model(chunks, gemini_client)

print(len(embeddings))
print(len(embeddings[0]))


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

