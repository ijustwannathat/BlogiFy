import requests
import random

with open('scripts/data.txt','r') as data:
    random_category = random.choice(data.readlines()).strip()
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={random_category}'
    api_key = '08FMOuC1+g3bGc5XYugC6w==yPC1QOAgvUkV5iAm'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    request_information = dict(*response.json())
    quote = request_information.get('quote')
    author = request_information.get('author')
    category = request_information.get('category')
