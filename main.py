import requests
import json

# using API key from rb_integrate app

api_key='29358c89451eb131c93c518694bd2317'
token='ATTA6d977895de70849f99491acfb2a3d37135bd7de5a8965f9c5c6a75a1a0e4fbdb702ADA4D'

#boards endpoint
get_url = f'https://api.trello.com/1/members/me/boards?key={api_key}&token={token}'

response = requests.get(get_url)

json_data = json.loads(response.content)
print(json_data)