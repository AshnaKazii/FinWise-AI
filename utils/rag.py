from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from utils.ai import ask_ai


VECTOR_STORE_PATH = "vector_store"


def load_vector_store():
    """
    Load existing FAISS vector database
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store



def ask_rag(question):
    """
    Retrieve relevant financial context and ask LLM
    """

    try:

        vector_store = load_vector_store()

        # Find relevant chunks
        results = vector_store.similarity_search(
            question,
            k=2
        )

        context = "\n\n".join(
            [doc.page_content for doc in results]
        )


        prompt = f"""
You are FinWise AI, a financial assistant.

Use the following financial document information to answer the user's question.

Financial Context:
------------------
{context}

User Question:
--------------
{question}

Provide a clear and personalized financial analysis.
"""


        response = ask_ai(prompt)

        return response


    except Exception as e:
        return f"❌ RAG Error: {str(e)}"