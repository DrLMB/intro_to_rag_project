import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="MY_OPENAI_API_KEY",
    model_name="text-embedding-3-small"
)

client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="project_docs", embedding_function=openai_ef)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

pdf_files = ["data/The_King’s_Challenge.pdf", "data/The_Rise_of_Aridoria.pdf", "data/The_Youngest_Prince's_Journey.pdf"]

for pdf_path in pdf_files:
    print(f"Processing {pdf_path}...")
    
    reader = PdfReader(pdf_path)
    docs_to_add = []
    ids_to_add = []
    metadatas_to_add = []
    
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if not page_text.strip():
            continue
            
        chunks = text_splitter.split_text(page_text)
        
        for chunk_index, chunk in enumerate(chunks):
            chunk_id = f"{pdf_path}_pg{i+1}_ch{chunk_index}"
            
            docs_to_add.append(chunk)
            ids_to_add.append(chunk_id)
            metadatas_to_add.append({"source": pdf_path, "page": i + 1})
            
    if docs_to_add:
        collection.add(
            documents=docs_to_add, 
            ids=ids_to_add,
            metadatas=metadatas_to_add
        )
        print(f"Added {len(docs_to_add)} chunks from {pdf_path}.")

print("All files added to database successfully.")