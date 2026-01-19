import os
from dotenv import load_dotenv
from openai import OpenAI
import datetime
from src.retrieval import ask_question 

load_dotenv()
client = OpenAI(api_key=os.getenv("MY_OPENAI_API_KEY"))

query = "What are some of the key events in the history of Aridoria?"

retrieved_context, _ = ask_question(query)

# defines the persona/system instructions/any further context
system_instruction = """
You are a specialized research assistant. The user is a researcher working on critical 
document analysis. Your goal is to provide academic, precise, and highly detailed 
answers based ONLY on the provided context. If the context is insufficient, 
explain what is missing rather than guessing.
"""

# calls the OpenAI API and generates response
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": system_instruction},
    {"role": "user", "content": f"Context: {retrieved_context}\n\nQuestion: {query}"}
  ],
  temperature=0 #to keep responses straightforward 
)

answer = response.choices[0].message.content
print(answer)

# creates a formatted log entry and add to research_journal.md
log_entry = f"""
### Research Session: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
**Question:** {query}
**Response:** {answer}
---
"""

with open("research_journal.md", "a", encoding="utf-8") as f:
    f.write(log_entry)

print("Successfully saved to research_journal.md")