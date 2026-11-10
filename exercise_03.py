import requests
url = 'https://jsonplaceholder.typicode.com/posts'

def fetch_post(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.Timeout:
        print('Request timed out.')
    except requests.HTTPError as e:
        print('HTTP error occurred.', e)
    except requests.ConnectionError as e:
        print('Connection failed.',e)

result = fetch_post(url)
print(result)