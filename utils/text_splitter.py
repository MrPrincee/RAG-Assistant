from langchain_text_splitters import RecursiveCharacterTextSplitter

def text_splitter(full_text:str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1650,
        chunk_overlap =170
    )
    chunks = splitter.split_text(full_text)

    return chunks

