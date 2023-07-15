import requests
import json

#requests
url = 'https://rickandmortyapi.com/api'
r = requests.get(url)
j = r.json()