import requests
url = "https://api.example.com/users"
api_key = "YOUR_API_KEY"

# headers = {
#     'x-api-key': api_key            #-------------- authentication through API key
# }
# response = requests.get(url, headers=headers)
# response.raise_for_status()
# --------------------------------------------------------------------------------------
headers = {
    'Authorization': 'Bearer api_key'              #-------------- authentication through token and bearer
           }                                 
response = requests.get(url, headers=headers)
response.raise_for_status()
# --------------------------------------------------------------------------------------
response = requests.get(url, auth=('username', 'password'))  #-------------- authentication through username and password
response.raise_for_status()
