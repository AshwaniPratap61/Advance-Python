import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    'Accept' : 'application/json'
}

response = requests.get(url, headers=headers)
# print(response.headers)
print(response.json())