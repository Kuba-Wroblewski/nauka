#!/usr/bin/python3
import requests
import json
from pprint import pprint
import webbrowser
from datetime import datetime, timedelta

'''
API - Aplication Programming Interface 
(interface to jest cos co widzisz mozesz z tego kozystac i nie wiesz jak działa)
Inter - pomiędzy
Face - twarz

time stamp - znak czasu
od 1 stycznia 1970

'''
# minimalnie 15 pkt
# poregregować malejąco
# z ostatniego tygodnia
# kategoria python

timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore
print(searchDate)
czasX = int(searchDate.timestamp())

params = {
    'site' : 'stackoverflow',
    'sort' : 'votes',
    'order' : 'desc',
    'fromdate' : czasX,
    'tagged' : 'python',
    'min' : 6

}



r = requests.get('https://api.stackexchange.com/2.3/questions', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    for question in questions['items']:
        pprint(question['link'])
        webbrowser.open_new_tab(question['link'])

