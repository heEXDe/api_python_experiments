import requests
import json

def api_fn():
    global key
    # has the API key been choosen?
    if key == 0:
        key = input(f'\n Insert your Yahoo Finance API key: \n')
    
    # choose an action
    actions = f'\n Choose an action (no space at the end): \n get current price - get the info \n v - veriosn of the program \n exit - exit the program'
    print(actions)    
    # btc_usd_dict = 0
    inp = input()
    if inp == 'get current price':
        # Getting the response from API
            response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"BTC-USD"})

            # Get the current price
            a =  list(json.loads(response.text).values())[0]
            a = dict(a).values()
            a = list(a)[0]
            a = a[0]
            a = a.get("regularMarketPrice")
            # Printing the output
            print(f'\n Yahoo Finance (BTC-USD) \n Current price: {a} [USD/BTC] \n')
            
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


key = 0
api_fn()

