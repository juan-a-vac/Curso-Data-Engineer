import requests
import json

#requests
url = 'https://fakestoreapi.com/products/1'
r = requests.get(url)
j = r.json()
print(j)