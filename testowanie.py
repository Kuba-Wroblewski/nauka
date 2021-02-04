#!/usr/bin/python3

import json

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


codingToJson = json.dumps(people, ensure_ascii=False)
# print(codingToJson)




# with open("testowyPlik_json", "w", encoding="UTF-8") as file:
#     json.dump(codingToJson, file, ensure_ascii=False)

# odczytjson = json.loads(codingToJson)
# print(odczytjson)

with open("testowyPlik_json", "r") as file:
    encoding = json.load(file)
print(encoding)



