#!/usr/bin/python3

import requests
import json
import webbrowser
from pprint import pprint

print("````Menu````")
how_much = int(input("Type number how much facts you want to see (min = 2)\n"))
which_animal = str(input("Which animal? (better 'cat' or 'dog')\n"))

params = {
    "amount": how_much,
    "animal_type": which_animal
}

r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for animal in content:
        print(animal["text"])
