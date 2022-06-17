import requests
import json

def api_fn2():
    global key
    # has the API key been choosen?
    if key == 0:
        key = input(f'\n Insert your IMDb API key: \n')
    
    # choose an action
    actions = f'\n Choose an action (no space at the end): \n gbt - get a movie by a title \n v - current version of the program \n exit - exit the program'
    print(actions)
    inp = input()
    # if gbt has been choosen
    if inp == 'gbt':
        # Getting the response from API
        title = input('Title to search for (small letters, no quotes, spaces but not at the end):')
        to_response = ''.join(['https://imdb-api.com/en/API/Search/', key, '/', title])
        response = requests.get(to_response)
        # Printing the output
        print(f'\n IMDb \n basic response: \n {response.text} \n')
        # Repeating the function
        api_fn2()
    # if get version of the program's been choosen
    elif inp == 'v':
        print('1.0.0')
        api_fn2()
    # if exit function's been choosen
    elif inp == 'exit':
        print(f'Closing the program.')    
    else:
        print(f'An error occurred. You probably entered the command incorrectly (space at the end ?).')
        api_fn2()


def proc_json(in_json, goal):
        # Get the current price
        a =  list(json.loads(in_json.text).values())[0]
        a = dict(a).values()
        a = list(a)[0]
        a = a[0]
        a = a.get(goal)
        return a

key = 0
api_fn2()

