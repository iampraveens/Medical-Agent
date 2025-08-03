from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document


def create_text_splitter(chunk_size: int = 500, chunk_overlap: int = 20) -> RecursiveCharacterTextSplitter:
    """Create a text splitter with specified parameters."""
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def split_documents(documents: List[Document], chunk_size: int = 500, chunk_overlap: int = 20) -> List[Document]:
    """Split documents into chunks."""
    text_splitter = create_text_splitter(chunk_size, chunk_overlap)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks
