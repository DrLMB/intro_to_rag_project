from src.retrieval import retrieved_context, query
from openai import OpenAI
import datetime

client = OpenAI(api_key="MY_OPENAI_API_KEY")

# defines the persona/system instructions
system_instruction = """
You are a specialized research assistant. The user is a researcher working on critical 
document analysis. Your goal is to provide academic, precise, and highly detailed 
answers based ONLY on the provided context. If the context is insufficient, 
explain what is missing rather than guessing.
"""

# calls the OpenAI API
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": system_instruction},
    {"role": "user", "content": f"Context: {retrieved_context}\n\nQuestion: {query}"}
  ],
  temperature=0 # to keep responses straightforward
)

print(response.choices[0].message.content)

# create a formatted log entry and add to research_journal.md
log_entry = f"""
### Research Session: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
**Question:** {query}
**Source Context:** {retrieved_context[:200]}... 

**Response:**{response}

---
"""

with open("research_journal.md", "a", encoding="utf-8") as f:
    f.write(log_entry)

print("Successfully saved to research_journal.md")