import tiktoken

# 1. Mock Data: Simulating a bloated environment
MOCK_KNOWLEDGE_BASE = [
    "Doc 1: The company holiday policy allows 20 days of PTO.",
    "Doc 2: Office hours are 9 AM to 5 PM.",
    "Doc 3: IT support is available at extension 5555.",
    "Doc 4: The cafeteria serves lunch from 12 PM to 2 PM.",
    "Doc 5: Expense reports must be filed by the 5th of the month."
]

MOCK_HISTORY = [
    {"role": "user", "content": "Hi, what time is the office open?"},
    {"role": "assistant", "content": "The office is open from 9 AM to 5 PM."},
    {"role": "user", "content": "What about lunch?"},
    {"role": "assistant", "content": "The cafeteria serves lunch from 12 PM to 2 PM."}
]

def count_tokens(text: str) -> int:
    """Helper to measure token usage."""
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

class BaselineAgent:
    def __init__(self):
        self.history = MOCK_HISTORY.copy()
        
    def generate_prompt(self, query: str) -> str:
        # BASELINE: Appends ALL documents and ALL history
        context = "\n".join(MOCK_KNOWLEDGE_BASE)
        history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history])
        
        prompt = f"Context:\n{context}\n\nHistory:\n{history_str}\n\nUser Query: {query}\nAnswer:"
        return prompt

    def run(self, query: str):
        prompt = self.generate_prompt(query)
        input_tokens = count_tokens(prompt)
        
        # Simulating LLM response
        mock_response = "Here is the answer based on the documents: You have 20 days of PTO."
        output_tokens = count_tokens(mock_response)
        
        # Update history
        self.history.append({"role": "user", "content": query})
        self.history.append({"role": "assistant", "content": mock_response})
        
        return {"input_tokens": input_tokens, "output_tokens": output_tokens, "response": mock_response}