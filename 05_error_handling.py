import requests
url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print('Connection timed out.')
except requests.exceptions.ConnectionError:
    print('Connection Error occured.')
except requests.exceptions.HTTPError as e:
    print('An HTTPError occured.', e)
except requests.exceptions.JSONDecodeError as e:
    print('Failed to convert into JSON.', e)
except requests.exceptions.RequestException as e:
    print('Failed request.', e)
    