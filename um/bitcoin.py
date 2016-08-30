import sys
import requests
import json
from pprint import pprint

def bitstamp_price(api_key):
    headers = {'content-type': 'application/json'}
    endpoint = "https://www.bitstamp.net/api/v2/ticker/btcusd/"
    r = requests.get(endpoint, headers=headers)
    json_data = json.loads(r.text) 
   
    return(json_data)



