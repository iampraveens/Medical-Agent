import os
from langchain_google_genai import ChatGoogleGenerativeAI


def get_chat_model(model_name: str = "models/gemini-2.5-flash") -> ChatGoogleGenerativeAI:
    """Initialize and return the chat model."""
    chat_model = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    return chat_model
