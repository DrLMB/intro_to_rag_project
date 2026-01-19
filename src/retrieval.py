from src.ingestion import collection

def ask_question(question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    
    # combine the found snippets into one single string of context
    retrieved_context = "\n\n".join(results['documents'][0])
    
    # returns these variables so that generation.py can use them
    return retrieved_context, question 