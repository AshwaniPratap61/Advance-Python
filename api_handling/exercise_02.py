import requests
import pandas as pd
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

#printing name and email
for info in data:
    print(info['name'], info['email'])

#user 1 city
print(data[0]['address']['city'])

# name of all the users
for names in data:
    print(names['name'])

# converting the response into dataframe
df = pd.DataFrame(data)
print(df.head())