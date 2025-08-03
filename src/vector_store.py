import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from typing import List
from langchain.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def create_pinecone_index(index_name: str):
    """Create a Pinecone index if it doesn't exist."""
    pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    
    if not pinecone.has_index(index_name):
        pinecone.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    
    pinecone_index = pinecone.Index(index_name)
    return pinecone_index


def store_embeddings(documents: List[Document], index_name: str, embeddings: GoogleGenerativeAIEmbeddings) -> PineconeVectorStore:
    """Store document embeddings in Pinecone vector store."""
    vector_store = PineconeVectorStore.from_documents(
        documents=documents,
        index_name=index_name,
        embedding=embeddings
    )
    return vector_store