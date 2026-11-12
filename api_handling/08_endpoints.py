import requests
import pandas as pd
username = 'mojombo'
profile_url = f'https://api.github.com/users/{username}'

response = requests.get(profile_url, timeout= 10)
response.raise_for_status()
user = response.json()


repo_url = f'https://api.github.com/users/{username}/repos'
response = requests.get(repo_url, timeout= 10)
response.raise_for_status()
repos = response.json()

print('Username: ', user['login'])
print('Public Reposotaries: ', user['public_repos'])


repo_data = []
print('Repo Names ================================================')
for repo in repos:
    repo_data.append({
        'name': repo.get('name', 'unknown'),
        'language': repo.get('language', 'unknown'),
        'star_count': repo.get('stargazers_count', 0)
    })
print('Repositories fatched ', len(repos))
print('next_page', response.links.get('next',{}).get('url'))