import requests
url = "https://httpbin.org/html"

response = requests.get(url, timeout=10)
response.raise_for_status()
try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError as e:
    print('Invalid JSON', e)