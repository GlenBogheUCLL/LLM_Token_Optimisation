import time
from baseline import BaselineAgent
from optimized import OptimizedAgent

def evaluate():
    test_query = "How many days of PTO do I get?"
    
    # Run Baseline
    baseline_agent = BaselineAgent()
    start = time.time()
    base_result = baseline_agent.run(test_query)
    base_time = time.time() - start
    
    # Run Optimized
    optimized_agent = OptimizedAgent(top_k=1, history_window=2)
    start = time.time()
    opt_result = optimized_agent.run(test_query)
    opt_time = time.time() - start
    
    # Calculate Metrics
    input_saved = base_result['input_tokens'] - opt_result['input_tokens']
    input_reduction_pct = (input_saved / base_result['input_tokens']) * 100
    
    print("=== EXPERIMENT RESULTS ===")
    print(f"Query: '{test_query}'\n")
    
    print("BASELINE AGENT:")
    print(f"- Input Tokens: {base_result['input_tokens']}")
    print(f"- Output Tokens: {base_result['output_tokens']}")
    print(f"- Response: {base_result['response']}\n")
    
    print("OPTIMIZED AGENT:")
    print(f"- Input Tokens: {opt_result['input_tokens']}")
    print(f"- Output Tokens: {opt_result['output_tokens']}")
    print(f"- Response: {opt_result['response']}\n")
    
    print("=== SUMMARY METRICS ===")
    print(f"Total Tokens Saved: {input_saved + (base_result['output_tokens'] - opt_result['output_tokens'])}")
    print(f"Input Token Reduction: {input_reduction_pct:.1f}%")

if __name__ == "__main__":
    evaluate()