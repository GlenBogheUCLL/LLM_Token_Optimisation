from baseline import count_tokens, MOCK_KNOWLEDGE_BASE, MOCK_HISTORY

class OptimizedAgent:
    def __init__(self, top_k=1, history_window=2):
        self.history = MOCK_HISTORY.copy()
        self.top_k = top_k
        self.history_window = history_window
        
    def mock_retrieve(self, query: str):
        # OPTIMIZATION 1: RAG Compression (Top-K)
        # In a real app, this would be a vector search. Here we just return the first matching doc.
        return [doc for doc in MOCK_KNOWLEDGE_BASE if "PTO" in doc or "holiday" in doc][:self.top_k]

    def generate_prompt(self, query: str) -> str:
        # Get compressed context
        relevant_docs = self.mock_retrieve(query)
        context = "\n".join(relevant_docs)
        
        # OPTIMIZATION 2: Sliding Window (Truncate history)
        recent_history = self.history[-self.history_window:] if self.history_window > 0 else []
        history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_history])
        
        # OPTIMIZATION 3: Concise Output Prompting
        prompt = f"Context:{context}\nHistory:{history_str}\nQuery:{query}\nReply concisely:"
        return prompt

    def run(self, query: str):
        prompt = self.generate_prompt(query)
        input_tokens = count_tokens(prompt)
        
        # Simulating a more concise LLM response due to system prompt instructions
        mock_response = "20 days."
        output_tokens = count_tokens(mock_response)
        
        self.history.append({"role": "user", "content": query})
        self.history.append({"role": "assistant", "content": mock_response})
        
        return {"input_tokens": input_tokens, "output_tokens": output_tokens, "response": mock_response}