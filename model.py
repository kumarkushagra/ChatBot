import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def generate_response(input_text):
    data = {"inputs": input_text}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()[0]['generated_text']
