import requests

response = requests.get("http://localhost:8081")
print(response.json())
