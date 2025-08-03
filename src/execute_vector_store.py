from dotenv import load_dotenv
from src.document_loader import load_pdfs_from_directory, filter_to_minimal_docs
from src.text_processing import split_documents
from src.embeddings import get_embeddings
from src.vector_store import create_pinecone_index, store_embeddings
from config.settings import Config

load_dotenv()

def execute_vector_store():
    config = Config()

    # Load and process documents
    extracted_docs = load_pdfs_from_directory(config.DATA_DIR)
    minimal_docs = filter_to_minimal_docs(extracted_docs)
    text_chunks = split_documents(minimal_docs, config.CHUNK_SIZE, config.CHUNK_OVERLAP)
    
    # Initialize embeddings
    embeddings = get_embeddings()

    # Create Pinecone index
    pinecone_index = create_pinecone_index(config.PINECONE_INDEX_NAME)

    # Store embeddings in Pinecone
    vector_store = store_embeddings(text_chunks, config.PINECONE_INDEX_NAME, embeddings)

    return vector_store

if __name__ == "__main__":
    execute_vector_store()