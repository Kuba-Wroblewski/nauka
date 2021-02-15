#!/usr/bin/python3

import json
import pprint
import requests

listUrl = {'''
        https://flask.palletsprojects.com/en/1.1.x/quickstart/,
        https://docs.python.org/3/tutorial/errors.html,
        https://pypi.org/project/requests2/,
        https://www.google.pl/,
        https://www.ggoooggllee.pl/,
        '''}

UrlNotFound = []
def czeck_url(url):
    response = requests.get(url)
    if response.status_code == 404:
        print("Nie ma takiej strony")
        UrlNotFound.append(url)
        print(UrlNotFound)
        # with open("listNotFoundUrl.txt", "w") as file:
            # file.writelines(UrlNotFound)
    else:
        print("A ta stronka jest")


czeck_url('https://docs.python.org/3/tutorial/inputoutput.htmll')
