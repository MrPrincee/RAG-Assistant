from pinecone import Pinecone,ServerlessSpec
import os
from dotenv import load_dotenv


load_dotenv()


def create_index(name:str,dimension:int,metric:str) -> None:

    pinecone_api_key = os.getenv("PINECONE_API_KEY")

    pinecone_client = Pinecone(api_key=pinecone_api_key)

    pinecone_client.create_index(
        name=name,
        dimension=dimension,
        metric=metric,
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )