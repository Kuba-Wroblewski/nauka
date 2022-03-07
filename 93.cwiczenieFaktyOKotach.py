#!/usr/bin/python3
import requests
import json
import webbrowser
from enum import IntEnum

'''
zrobic menu 
z zapytaniem czy ma wyswietlic przykładowe fakty o psach czy kotach
i zalezne od wyboru to 5 dowolnych faktów na temat zwierzecia wybranego
'''

menu = IntEnum("menu_animals", "Facts Photo Exit")

while True:
    odpowiedz = float(input("""\nDo You wont to see some random facts of dogs ?
    Or maybe You wont to see random photo of dog ?\n

1 - Facts
2 - Photo
3 - Exit program\n"""))

    if odpowiedz == menu.Facts:

        params = {'number': 5}
        r = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs', params)

        try:
            animalSite = r.json()
        except json.decoder.JSONDecodeError:
            print('Bad site')
        else:
            for animal in animalSite:
                print('\n', animal)
    elif odpowiedz == menu.Photo:

        r = requests.get('https://random.dog/woof.json')

        try:
            animalSite = r.json()
        except json.decoder.JSONDecodeError:
            print('Bad site')
        else:
            for animal in animalSite:
                print('\n', animalSite['url'])
                webbrowser.open_new_tab(animalSite['url'])
                break

    elif odpowiedz == menu.Exit:
        print('Exit program')
        break
    else:
        print('Your choice is not correct. choose one of thre options from Menu')
