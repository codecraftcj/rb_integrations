import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# using API key from rb_integrate app

api_key= config.get('TRELLO API','api_key')
token=config.get('TRELLO API','token')

#boards endpoint
get_url = f'https://api.trello.com/1/members/me/boards?key={api_key}&token={token}'

response = requests.get(get_url)

json_data = json.loads(response.content)
print(json_data)