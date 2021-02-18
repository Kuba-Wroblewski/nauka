#!/usr/bin/python3

import requests

listUrl = [ 'https://flask.palletsprojects.com/en/1.1.x/quickstart/', 'https://github.com/fuck', 'https://www.google.pl/', 'https://www.google.pl/nocos' ]

def checkUrl(listUrl):
    UrlNotFound = []
    for element in listUrl:
        response = requests.get(element)
        if response.status_code == 200:
            UrlNotFound.append(element)
            UrlNotFound.append("\n")
            with open('listNotFoundUrl.txt', 'w') as file:
                file.writelines(UrlNotFound)

checkUrl(listUrl)