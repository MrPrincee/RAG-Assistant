import time

from google.genai import types


def embedding_model(chunks: list[str], gemini_client) -> list[list[float]]:
    embeddings_list = []
    batch_size = 20

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        contents = []

        for chunk in batch:
            content = types.Content(
                parts=[
                    types.Part.from_text(text=chunk)
                ]
            )
            contents.append(content)

        result = gemini_client.models.embed_content(
            model="gemini-embedding-2",
            contents=contents
        )

        for embedding in result.embeddings:
            embeddings_list.append(embedding.values)

        print(f"Processed {len(embeddings_list)}/{len(chunks)} chunks")

        time.sleep(20)

    return embeddings_list