from src.ingestion import collection

query = ""
results = collection.query(query_texts=[query], n_results=5)

retrieved_context = " ".join(results['documents'][0])

def ask_question(question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    print(f"\n--- Results for: '{question}' ---")
    
    for i in range(len(results['documents'][0])):
        content = results['documents'][0][i]
        metadata = results['metadatas'][0][i]
        distance = results['distances'][0][i]
        
        print(f"\nResult #{i+1} (Score: {distance:.4f})")
        print(f"Source: {metadata['source']} | Page: {metadata['page']}")
        print(f"Snippet: {content[:200]}...") 
        print("-" * 30)

ask_question("What are some of the key events in the history of Aridoria?")