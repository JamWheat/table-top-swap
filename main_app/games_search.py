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
    if isinstance(each['name'], str):
      if 'yearpublished' in each:
        response.append([each['@objectid'], each['name'], each['yearpublished']])
      else:
        response.append([each['@objectid'], each['name'], 0000])
    else:
      if 'yearpublished' in each:
        response.append([each['@objectid'], each['name']['#text'], each['yearpublished']])
      else:
        response.append([each['@objectid'], each['name']['#text'], 0000])
  return response

def find(query):
  search = requests.get(f'{base_url}boardgame/{query}')
  search_xml = xmltodict.parse(search.text)
  search_json_dumps = json.dumps(search_xml)
  search_json_dict = json.loads(search_json_dumps)
  response = {}
  response['bgg_slug'] = search_json_dict['boardgames']['boardgame']['@objectid']
  response['year_published'] = search_json_dict['boardgames']['boardgame']['yearpublished']
  response['thumbnail'] = search_json_dict['boardgames']['boardgame']['thumbnail']
  response['image'] = search_json_dict['boardgames']['boardgame']['image']
  return response