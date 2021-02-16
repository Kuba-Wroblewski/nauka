#!/usr/bin/python3

import requests
import json
import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos')

try:
    event = response.json()
except json.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszsytko okej")
    print(event[0])
