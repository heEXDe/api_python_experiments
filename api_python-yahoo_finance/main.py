import requests
import json

def api_fn():
    global key
    # has the API key been choosen?
    if key == 0:
        key = input(f'\n Insert your Yahoo Finance API key: \n')
    
    # choose an action
    actions = f'\n Choose an action (no space at the end): \n btc-usd - get current info for BTC/USD pair \n eth-usd - get current info for ETH/USD pair \n ixic-usd - get current info for IXIC/USD (NASDAQ) pair \n v - current version of the program \n exit - exit the program'
    print(actions)
    inp = input()
    # if btc-usd's been choosen
    if inp == 'btc-usd':
        # Getting the response from API
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"BTC-USD"})
        # Printing the output
        print(f'\n Yahoo Finance (BTC-USD) \n Current price: {proc_json(response, "regularMarketPrice")} [USD/BTC] \n Two hundred day average: {proc_json(response, "twoHundredDayAverage")} [USD/BTC] \n')
        # print(f'\n SOMETHING EXTRA: \n {json.loads(response.text)} \n')
        # Repeating the function
        api_fn()
    # if eth-usd's been choosen
    elif inp == 'eth-usd':
        # Getting the response from API
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"ETH-USD"})
        # Printing the output
        print(f'\n Yahoo Finance (ETH-USD) \n Current price: {proc_json(response, "regularMarketPrice")} [USD/ETH] \n Two hundred day average: {proc_json(response, "twoHundredDayAverage")} [USD/ETH]')
        # Repeating the function
        api_fn()
    # if eth-usd's been choosen
    elif inp == 'ixic-usd':
        # Getting the response from API
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"^IXIC"})
        # Printing the output
        print(f'\n Yahoo Finance (^IXIC) \n Current price: {proc_json(response, "regularMarketPrice")} [USD/^IXIC] \n Two hundred day average: {proc_json(response, "twoHundredDayAverage")} [USD/^IXIC]')
        # Repeating the function
        api_fn()
    # if get version of the program's been choosen
    elif inp == 'v':
        print('1.0.0')
        api_fn()
    # if exit function's been choosen
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

