import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/users'
params = {
    '_limit': 5
}
user_data = requests.get(url, params=params)
df = pd.DataFrame(user_data.json())
print(df)
