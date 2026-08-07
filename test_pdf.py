from utils.pdf_reader import extract_text_from_pdf


pdf_path = "documents/sample_statement.pdf"

with open(pdf_path, "rb") as file:
    extracted_text = extract_text_from_pdf(file)

print("PDF TEXT EXTRACTION TEST")
print("-" * 40)

if extracted_text:
    print("✅ PDF extraction successful\n")
    print(extracted_text[:1000])
else:
    print("❌ No text extracted from PDF")