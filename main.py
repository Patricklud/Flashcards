import requests
import json

# Replace with your Mac's IP address or hostname
OLLAMA_HOST = "http://your_mac_ip_or_hostname:11434"

def query_ollama(prompt, model="nous-hermes"):
    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(f"{OLLAMA_HOST}/api/generate", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Example usage
try:
    prompt = "Generate an interview question about Python."
    response = query_ollama(prompt)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")