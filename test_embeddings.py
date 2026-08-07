from utils.pdf_reader import extract_text_from_pdf
from utils.embeddings import create_embeddings


pdf_path = "documents/sample_statement.pdf"


with open(pdf_path, "rb") as file:
    text = extract_text_from_pdf(file)


print("Creating embeddings...")

vector_store = create_embeddings(text)

print("✅ Embeddings created successfully")