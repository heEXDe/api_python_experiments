import requests
import json

def rest_fn():
    key = input(f'\n Insert your Yahoo Finance API key: \n')
    actio = input(f'\n Decide what you want to do: /n get - get the info \n')
    if actio == 'get':
        # api_url = "https://yfapi.net/v6/finance/quote/BTC-USD"
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"BTC-USD"})
        return f'\n Yahoo Finance \n BTC-USD: \n STATUS CODE: \n {response.status_code} \n RESPONSE TEXT: \n {response.text} \n'

print(rest_fn())

