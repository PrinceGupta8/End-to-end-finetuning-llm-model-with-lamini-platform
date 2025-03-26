
import lamini
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
lamini_api_key = os.getenv('LAMINI_API_KEY')  # Ensure correct variable name

# Correct way to initialize the Lamini LLM
llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct", api_key=lamini_api_key)

# Training Data
data = [
    {"input": "What is machine learning?", "output": "Machine learning is a subset of AI that enables computers to learn from data."},
    {"input": "Explain neural networks.", "output": "Neural networks are computing systems inspired by the human brain, used in deep learning."}
]

# Fine-tune the model
llm.tune(data)

# Invoke the fine-tuned model
response = llm.generate({'input': 'What is machine learning?'})
print(response)
