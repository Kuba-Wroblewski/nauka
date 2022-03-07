#!/usr/bin/python3

import requests

"""
pip - pip installs package - instalator pakunków
PyPi - Python Package index - index (spis) pakunków do Pythona

"""

response = requests.get("https://flask.palletsprojects.com/en/1.1.x/quickstart/")
response.status_code

print(response)

# status_code = 200 - łączy się ze stroną, strona istnieje
# status_code = 404 - nie łączy się, nie ma takiej strony
