from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def load_existing_vector_store(index_name: str, embeddings: GoogleGenerativeAIEmbeddings) -> PineconeVectorStore:
    """Load an existing Pinecone vector store."""
    vector_store = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    return vector_store

def create_retriever(vector_store: PineconeVectorStore, search_type: str = "similarity", k: int = 10):
    """Create a retriever from the vector store."""
    retriever = vector_store.as_retriever(
        search_type=search_type, 
        search_kwargs={"k": k}
    )
    return retriever