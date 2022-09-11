import requests
import json


def identify_smartest(*args):
    base_url = 'https://akabab.github.io/superhero-api/api'
    all_superheroes = '/all.json'
    response = requests.get(f'{base_url}{all_superheroes}')
    heroes_base = json.loads(response.text)

    intelligence = {}
    smartest = ''
    for name in args:
        for hero in heroes_base:
            if hero['name'] == name:
                intelligence[name] = hero['powerstats']['intelligence']
    max_intelligence = max(intelligence.values())
    for hero in intelligence:
        if intelligence[hero] == max_intelligence:
            if not smartest:
                smartest = hero
            else:
                smartest += f', {hero}'
    return f'The smartest guy is {smartest}' if ',' not in smartest else f'The smartest guys are {smartest}'


if __name__ == '__main__':
    print(identify_smartest('Batman', 'Captain America', 'Spider Man', 'Thanos', 'Hulk', 'Страшила', 'Ctulhu'))
