import json
import requests

with open('scripts/posts_load.json', 'r+') as data:
    json_data = json.load(data)
    url = 'http://127.0.0.1:8000/api/'
    for i in json_data:
        response = requests.post(url, json=i)
        print(response)

