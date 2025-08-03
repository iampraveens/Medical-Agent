import os
from dataclasses import dataclass


@dataclass
class Config:
    # Directories
    DATA_DIR: str = "data"
    
    # Pinecone settings
    PINECONE_INDEX_NAME: str = "medical-agent"
    PINECONE_DIMENSION: int = 768
    PINECONE_METRIC: str = "cosine"
    PINECONE_CLOUD: str = "aws"
    PINECONE_REGION: str = "us-east-1"
    
    # Text processing
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 20
    
    # Retrieval
    RETRIEVAL_K: int = 10
    
    # Models
    EMBEDDING_MODEL: str = "models/embedding-001"
    CHAT_MODEL: str = "models/gemini-2.5-flash"
    
    # API Keys (loaded from environment)
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
