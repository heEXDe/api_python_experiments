import requests
import json

def api_fn():
    global key
    if key == 0:
        key = input(f'\n Insert your Yahoo Finance API key: \n')
    actions = f'\n Choose an action: \n get - get the info \n v - veriosn of the program \n exit - exit the program'
    print(actions)
    inp = input()
    if inp == 'get':
        response = requests.get("https://yfapi.net/v6/finance/quote", headers={'x-api-key': key}, params={"symbols":"BTC-USD"})
        print(f'\n Yahoo Finance (BTC-USD) \n Status code: \n {response.status_code} \n Response JSON deserialized to what data type: \n {type(json.loads(response.text))} \n ')
        # RESPONSE JSON: \n {response.json()} \n RESPONSE DESERIALIZED: \n {json.loads(response.text)}
        api_fn()
    elif inp == 'v':
        print('1.0.0')
        api_fn()
    elif inp == 'exit':
        print(f'Closing the program.')
    else:
        api_fn()


key = 0
api_fn()

