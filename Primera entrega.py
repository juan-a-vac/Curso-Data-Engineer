#info tomada de https://www.frankfurter.app/
import requests
import json

#requests
url = 'https://www.frankfurter.app/latest'
r = requests.get(url)
j = r.json()
print(j)
#print(j.keys())
#dict_keys(['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR'])
