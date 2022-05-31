import requests
import json

def api_fn():
    global key
    # has the API key been choosen?
    if key == 0:
        key = input(f'\n Insert your Yahoo Finance API key: \n')
    
    # choose an action
    actions = f'\n Choose an action (no space at the end): \n gcp-btc - get current price of BTC/USD \n gcp-eth - get current price of ETH/USD \n v - current version of the program \n exit - exit the program'
    print(actions)    
    # btc_usd_dict = 0
    inp = input()
    if inp == 'gcp-btc':
        # Getting the response from API
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"BTC-USD"})
        # Printing the output
        print(f'\n Yahoo Finance (BTC-USD) \n Current price: {proc_json(response, "regularMarketPrice")} [USD/BTC] \n')
        # Repeating the function
        api_fn()
    elif inp == 'gcp-eth':
        # Getting the response from API
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"ETH-USD"})
        # Printing the output
        print(f'\n Yahoo Finance (BTC-USD) \n Current price: {proc_json(response, "regularMarketPrice")} [USD/ETH] \n')
        # Repeating the function
        api_fn()
    elif inp == 'v':
        print('1.0.0')
        api_fn()    
    elif inp == 'exit':
        print(f'Closing the program.')    
    else:
        print(f'An error occurred. You probably entered the command incorrectly (space at the end ?).')
        api_fn()


def proc_json(in_json, goal):
        # Get the current price
        a =  list(json.loads(in_json.text).values())[0]
        a = dict(a).values()
        a = list(a)[0]
        a = a[0]
        a = a.get(goal)
        return a

key = 0
api_fn()

