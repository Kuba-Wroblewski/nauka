#!/usr/bin/python3
import requests
import json
import pprint

'''
API - Aplication Programming Interface 
(interface to jest cos co widzisz mozesz z tego kozystac i nie wiesz jak działa)
Inter - pomiędzy
Face - twarz

'''

# minimalnie 6 pkt
# poregregować malejąco
# z ostatniego tygodnia
# kategoria python

params = {
    'site': 'stackoverflow',
    'sort': 'votes',
    'order': 'desc',
    'fromdate': '2021-09-06',
    'tagged': 'python',
    'min': 6

}

r = requests.get('https://api.stackexchange.com/2.3/questions', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    pprint.pprint(questions)
