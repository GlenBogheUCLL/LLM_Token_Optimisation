# LLM_Token_Optimisation

## Overview
This repository contains the deliverables for the short technical exercise on optimizing token usage in an AI agent.

The project investigates approaches for reducing the input and output token usage of an LLM-based operational knowledge assistant while maintaining the quality and reliability of its answers.

## Context
The AI assistant answers user questions using retrieved information from an organization's internal knowledge sources. A typical prompt payload includes system instructions, conversation history, retrieved documents, the user's question, and the generated response. As these elements grow, token usage scales up, necessitating optimization.

## How to Run the Proof of Concept

This repository includes a lightweight, mock-based Proof of Concept (PoC) written in Python. It demonstrates the exact token savings of the proposed techniques without requiring API keys or a live vector database.

### Prerequisites
The only external dependency is `tiktoken`, which is used to accurately simulate OpenAI's token-counting logic.

1. Ensure you have Python 3.7+ installed.
2. Install the required tokenizer library:
   ```bash
   pip install tiktoken
3. Running the evaluation script
    ```bash
   python src/evaluate.py
