

import requests

url = "https://imsea.herokuapp.com/api/1?q="

async def ImageSearch(name, idx):
    new_url = url + name
    response = requests.get(new_url)
    pics = response.json()["results"]
    pics = pics[::2]
    result = pics[idx*10:(idx+1)*10]
    
    return result





