import requests as r
url = 'http://api.github.com/user_not_exit'
try:
    response = r.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)
except r.exceptions.HTTPError as e:
    print('HTTP error occured', e)