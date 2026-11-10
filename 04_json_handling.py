import requests
import pandas as pd

data = {
    "id": 1,
    "name": "Boss",
    "email": "boss@example.com",
    "address": {
        "city": "Bhopal",
        "zipcode": "462001"
    }
}

data2 = [
    {"id": 1, "name": "Boss"},    #----- index 0
    {"id": 2, "name": "Alex"},
    {"id": 3, "name": "Sam"}
]
# print(data['id'], data['name'])
# print(data['address']['city'], data['address']['zipcode'])
# print(data2[2]['name'])
for user in data:
    print(user)

# looping
for key, values in data.items():
    print(key, values)