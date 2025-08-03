from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from typing import List
from langchain.schema import Document


def load_pdfs_from_directory(directory: str) -> List[Document]:
    """Load all PDF documents from a directory."""
    loader = DirectoryLoader(directory, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """Filter documents to keep only essential metadata."""
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get('source')
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={'source': src}
            )
        )
    return minimal_docs
