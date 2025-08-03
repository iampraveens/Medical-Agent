from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


def create_document_chain(llm: ChatGoogleGenerativeAI, prompt: ChatPromptTemplate):
    """Create a document processing chain."""
    chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )
    return chain


def create_full_retrieval_chain(retriever, document_chain):
    """Create the complete retrieval chain."""
    retrieval_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=document_chain
    )
    return retrieval_chain
