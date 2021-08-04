import hashlib
import json

WIKIPEDIA_LINKS = 'Task.txt'
COUNTRIES = 'countries.json'
WIKI_URL = 'https://en.wikipedia.org/wiki/'


class Countries:

    def __init__(self, country_file):
        with open(country_file) as file:
            text = json.load(file)
            country_names = (country['name']['common'] for country in text)
            self.country_names_iter = iter(country_names)

    def get_link(self, country_name: str):
        country_name = country_name.replace(' ', '_')
        url = f'{WIKI_URL}{country_name}'
        return url

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.country_names_iter)
        res = f'{country_name} - {self.get_link(country_name)}'
        return res

def get_hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    with open(WIKIPEDIA_LINKS, 'w') as file:
        for item in Countries(COUNTRIES):
             print(item)
             file.write(f'{item}\n')

    for hash_str in get_hash(WIKIPEDIA_LINKS):
        print(hash_str)










