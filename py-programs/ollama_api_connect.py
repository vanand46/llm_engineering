import requests
import json
import textwrap

# Constants
OLLAMA_API_URL = "http://localhost:11434/api/chat"
HEADERS = { "Content-Type": "application/json" }
MODEL_NAME = "llama3.2"

def chat_with_ollama(prompt, model=MODEL_NAME, stream=False, width=80):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": stream
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        data = response.json()
        
        content = data.get('message', {}).get('content')
        if content:
            print("\n" + "=" * width)
            print("💬 Response from Ollama:\n")
            print(textwrap.fill(content, width=width))
            print("=" * width + "\n")
            return content
        else:
            print("No content returned from Ollama.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Usage
chat_with_ollama("Show some of the business applications of Generative AI")
