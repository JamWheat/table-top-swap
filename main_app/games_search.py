import requests
import xmltodict
import json

base_url = 'http://www.boardgamegeek.com/xmlapi/'

def search(query):
  search = requests.get(f'{base_url}search?search={query}')
  search_xml = xmltodict.parse(search.text)
  search_json_dumps = json.dumps(search_xml)
  search_json_dict = json.loads(search_json_dumps)
  response = []
  for each in search_json_dict['boardgames']['boardgame']:
    response.append(game['name']['#text'])
  return response