import urllib.request
import json

def query_ollama(prompt, model="nous-hermes2"):
    url = "http://localhost:11434/api/generate"
    data = json.dumps({"model": model, "prompt": prompt}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        json_responses = [json.loads(line) for line in response_data.strip().split('\n')]
        
        full_response = ''.join(resp.get('response', '') for resp in json_responses)
        return full_response

try:
    response = query_ollama(
        "You are an expert in finance, python, SQL, banking, and financial modeling. You are also a phenomenal, thought-provoking mentor who is helping this user prepare for a technical interview in finance, banking, financial modeling, python, and SQL. Generate 100 questions and answers for technical questions pertaining to these topics. Consider typical tools that might be used in these roles, and make sure the answers are succinct yet answer the question in depth, and include short code if necessary for the question."
        )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")