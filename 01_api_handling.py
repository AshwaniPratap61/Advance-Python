import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# -------- converting json response to data frame ----------------
# df = pd.DataFrame(response.json())
# print(df)

# -------- http get method ----------------
# print(response.status_code)
# print(response.json())

# -------- http post method---------------
# payload = {
#     'name': 'boss',
#     'username': 'boss0999',
#     'email': 'boss@gmail.com' 
# }        
# new_user = requests.post(url, json= payload)
# print(new_user.json())
# ------------------------------------------------------------

# print(response.status_code)
print(response.json())
# ------------------------------------------------------------



