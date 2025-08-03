from dotenv import load_dotenv
load_dotenv()

from src.embeddings import get_embeddings
from src.retrieval import load_existing_vector_store, create_retriever
from src.llm_inference import get_chat_model
from src.prompts import get_medical_prompt
from src.chain import create_document_chain, create_full_retrieval_chain
from config.settings import Config

def main():
    config = Config()
    
    # Initialize embeddings
    embeddings = get_embeddings()

    # Load existing vector store
    vector_store = load_existing_vector_store(config.PINECONE_INDEX_NAME, embeddings)

    # Create retriever
    retriever = create_retriever(vector_store, k=config.RETRIEVAL_K)

    # Get chat model and prompt
    llm = get_chat_model(config.CHAT_MODEL)
    prompt = get_medical_prompt()

    # Create document processing chain
    document_chain = create_document_chain(llm, prompt)

    # Create full retrieval chain
    retrieval_chain = create_full_retrieval_chain(retriever, document_chain)

    # Run retrieval chain
    response = retrieval_chain.invoke({
        "input": "What is Acne? and how is it treated?"
    })
    print(response['answer'])
    
if __name__ == "__main__":
    main()