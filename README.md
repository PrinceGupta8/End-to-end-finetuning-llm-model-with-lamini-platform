# Lamini Fine-Tuning with LLaMA 3.1

This project demonstrates **fine-tuning** a **Meta-Llama-3.1-8B-Instruct** model using **Lamini**. It provides a simple example of training the model with structured data and generating responses from the fine-tuned model.

## Features

- Fine-tunes **Lamini LLM** on custom training data.
- Uses **Meta-Llama-3.1-8B-Instruct** model.
- Generates responses from the fine-tuned model.
- Utilizes **environment variables** for API key security.

## Installation

### Prerequisites

- Python 3.8+
- Pip
- Lamini API Key (Sign up at [Lamini](https://lamini.ai/))

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/lamini-finetuning.git
   cd lamini-finetuning
   ```

2. \*\*Create a virtual environment \*\*

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API Key**

   - Create a `.env` file in the root directory and add:
     ```
     LAMINI_API_KEY=your_lamini_api_key
     ```

## Usage

1. **Run the script**

   ```bash
   python fine_tune.py
   ```

2. **Example Output:**

   ```
   Fine-tuning in progress...
   Model fine-tuned successfully!
   Response: Machine learning is a subset of AI that enables computers to learn from data.
   ```

## Code Overview

### Load API Key

```python
from dotenv import load_dotenv
import os
load_dotenv()
lamini_api_key = os.getenv('LAMINI_API_KEY')
```

### Initialize Lamini Model

```python
import lamini
llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct", api_key=lamini_api_key)
```

### Define Training Data

```python
data = [
    {"input": "What is machine learning?", "output": "Machine learning is a subset of AI that enables computers to learn from data."},
    {"input": "Explain neural networks.", "output": "Neural networks are computing systems inspired by the human brain, used in deep learning."}
]
```

### Fine-Tune and Generate Response

```python
llm.tune(data)
response = llm.generate({'input': 'What is machine learning?'})
print(response)
```

## Contributing

Pull requests are welcome! Feel free to fork and improve this project.

## License

This project is licensed under the **MIT License**.

---

🚀 **Fine-tune AI models effortlessly with Lamini!**

