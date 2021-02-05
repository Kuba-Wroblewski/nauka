#!/usr/bin/python3

import json
import pprint

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

# Poniżej zapisane dane do json, w postaci stringa
codingJson = json.dumps(people, ensure_ascii=False)
print(codingJson, "\n")

pprint.pprint(codingJson)

# Odczytane dane z pliku json
encoding = json.loads(codingJson)
print(encoding)

# Zapisane dane w postaci json do pliku
with open("testowyPlik_json", "w", encoding="UTF-8") as file:
    json.dump(people, file, ensure_ascii=False)

# Odczytane dane z pliku json
with open("testowyPlik_json", "r") as file:
    wynik = json.load(file)
print(json.dumps(wynik, indent=4, ensure_ascii=False, sort_keys=True))

# Lub pprint aby kod wyglądał ładnie i był łatwy do odczytu
pprint.pprint(wynik)
