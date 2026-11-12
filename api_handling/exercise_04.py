import requests
username = 'mojombo'
url = f'https://api.github.com/users/{username}/repos?per_page=100'
all_repos = []

while url:
    response = requests.get(url, timeout= 10)
    response.raise_for_status()
    data = response.json()
    all_repos.extend(data)

    url = response.links.get('next', {}).get('url')

print(len(all_repos))