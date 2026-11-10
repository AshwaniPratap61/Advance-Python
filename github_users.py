import requests
from datetime import datetime
import time
url = "https://api.github.com/users?per_page=100"

all_users = [] 
target_users = 1000

while url and len(all_users)<target_users:
    response = requests.get(url, timeout=20)
    if response.status_code in (403, 429):
        remaining = response.headers.get('X-RateLimit-Remaining')
        retry_after = response.headers.get('Retry-After')
        if remaining == '0':
            reset= int(response.headers.get('X-RateLimit-Reset'))
            waiting_time = max(reset - time.time(), 0)
            time.sleep(waiting_time)
            continue
        elif retry_after:
            time.sleep(int(retry_after))
            continue
    response.raise_for_status()
    data = response.json()

    all_users.extend(data)
    all_users = all_users[:target_users]
    url = response.links.get('next', {}).get('url')
    print('users collected: ', len(data))

print('Final Length: ', len(all_users))
print(response.status_code)
print(response.text)