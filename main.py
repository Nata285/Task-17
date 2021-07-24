import json
import pprint

import requests
import wikipedia

class Countries:

    with open('countries.json','r',encoding='utf-8') as f:
         text = json.load(f)


    for i in text:
        name=i['name']['common']
        url = wikipedia.page(name).url
        print(f'{name}-{url}')



