#!/usr/bin/python3

import json
import pprint
import requests

people =  {
        "IcFDG2bO9AYDF651DoyH": {'name': 'Łukasz', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Łukasz', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
    }

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
        with open("listNotFoundUrl.txt", "w") as file:
            file.writelines()
    else:
        print("A ta stronka jest")



czeck_url("https://www.google.pl/")
