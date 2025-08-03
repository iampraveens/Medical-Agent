import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def get_embeddings() -> GoogleGenerativeAIEmbeddings:
    """Initialize and return Google Generative AI embeddings."""
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        request_options={
            "timeout": 10,
        }
    )
    return embeddings
