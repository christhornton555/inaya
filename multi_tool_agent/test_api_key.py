import requests
import json

# Get an API key at https://aistudio.google.com/apikey

# Replace this with your actual API key
api_key = "AIzaSyB7eDQB9clQmmkYuJH6tG8jUeqZjQRPF0k"

# Define the endpoint URL
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Define the payload
data = {
    "contents": [
        {
            "parts": [
                {"text": "Explain how AI works"}
            ]
        }
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response
if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=2))
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
