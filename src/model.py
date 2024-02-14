import json
import requests

def call_ollama(model, prompt, stream=False):
    url = 'http://localhost:11434/api/generate'
    
    data = {
        'model' : model,
        'prompt' : prompt,
        'stream' : stream}
    json_data = json.dumps(data)
    response = requests.post(url=url, data=data, 
                             headers={'content-Type':'application/json'})
    if response.status_code == 200:
        return response.json()
    
    else: return f'response Error code is {response.status_code}'