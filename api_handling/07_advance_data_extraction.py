import requests
url = "https://jsonplaceholder.typicode.com/posts"
all_posts = []
page = 1
limit = 100

while True:
    params = {
        '_page' : page,
        '_limit' : limit
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if not data:
        break
    else:
        all_posts.extend(data)
        page +=1

print(f'Total records {len(all_posts)}')