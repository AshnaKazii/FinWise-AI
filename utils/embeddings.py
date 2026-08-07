from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


VECTOR_STORE_PATH = "vector_store"


def create_embeddings(text):
    """
    Convert document text into embeddings and save FAISS index
    """

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    # Create embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vector store
    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    # Save locally
    vector_store.save_local(VECTOR_STORE_PATH)

    return vector_store