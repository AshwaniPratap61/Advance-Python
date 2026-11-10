import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/posts"

# paragm = {
#     'userId':3
#     }
# response = requests.get(url, params=paragm)
# print(response.json())
# --------------------------------------------------
# paragm = {
#     'userId':2,
#     '_limit' :4
#     }
# response = requests.get(url, params=paragm)
# print(response.json())

# headers = {
#     "Accept": "application/json",
#     'User-Agent': "BossPythonClient"
# }
# response = requests.get(url, headers=headers)
# print(response.json())
# --------------------------------------------------
paragm = {
    'userId':5,
    '_limit' : 3
    }
headers = {
    "Accept": "application/json"
}
response = requests.get(url, headers=headers, params=paragm)
df = pd.DataFrame(response.json())
print(df.shape)
