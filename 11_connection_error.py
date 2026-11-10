import requests
url= "http://127.0.0.1:9999"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.ConnectionError as e:
    print("Failed to connect to server", e)
