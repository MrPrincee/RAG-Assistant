from fastapi import FastAPI

from utils.pdf_reader import pdf_reader
from utils.create_index import create_index
from utils.gemini_client import get_gemini_client


#Gemini API client
gemini_client = get_gemini_client()


#extract text from PDF
full_text = pdf_reader("fruits.pdf")


# print(client.models.count_tokens(
#     model="gemini-embedding-2",
#     contents=full_text
# ))



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

