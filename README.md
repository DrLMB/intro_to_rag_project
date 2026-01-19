# intro_to_rag_project
An exercise in Retrieval-Augmented Generation (RAG) based on a portfolio project suggested in the Codecademy course Learn Prompt Engineering.

# PDF Research Assistant (RAG Pipeline)

A Python-based **Retrieval-Augmented Generation (RAG)** system designed to extract and analyze information from PDF documents. This tool uses **ChromaDB** for vector storage and **OpenAI's GPT-4o** to provide precise, evidence-based answers.

## 🚀 Features
- **PDF Ingestion:** Extracts text from PDFs and chunks it using `RecursiveCharacterTextSplitter`.
- **Vector Search:** Uses OpenAI `text-embedding-3-small` to store and retrieve document context.
- **Context-Aware Generation:** Uses a specialized system prompt to ensure responses are academic and strictly based on the provided documents.
- **Research Journal:** Automatically logs every research query and result into a persistent Markdown file.

## 🛠️ Tech Stack
- **LLM:** OpenAI GPT-4o
- **Vector Database:** ChromaDB
- **Text Processing:** LangChain (Text Splitters), PyPDF
- **Environment Management:** Python-dotenv

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>

```

2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Configure Environment Variables:**
Create a `.env` file in the root directory:
```env
MY_OPENAI_API_KEY=your_openai_api_key_here

```


4. **Prepare Data:**
Place your PDF files in a `data/` directory. By default, the script looks for the synthetic example files provided by Codecademy:
* `data/The_King’s_Challenge.pdf`
* `data/The_Rise_of_Aridoria.pdf`



---

## 📖 Usage

### 1. Ingest Documents

Run the ingestion script to process your PDFs, create embeddings, and build the local vector database (`/my_vector_db`).

```bash
python -m src.ingestion

```

### 2. Query and Generate

Run the generation script to perform a similarity search and get an answer from the LLM.

```bash
python -m src.generation

```

### 3. View Results

Check **`research_journal.md`** to see a formatted history of all your questions and the AI's responses.

---

## 📂 Project Structure

* `ingestion.py`: Processes PDFs and populates the ChromaDB collection.
* `retrieval.py`: Logic for querying the vector database for relevant snippets.
* `generation.py`: The main execution script that calls the OpenAI API and logs results.
* `research_journal.md`: An auto-generated log of research sessions.
* `requirements.txt`: List of necessary Python packages.

```
