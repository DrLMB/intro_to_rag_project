from src.ingestion import collection

query = ""
results = collection.query(query_texts=[query], n_results=2)

# extract the retrieved texts
retrieved_context = " ".join(results['documents'][0])