#!/usr/bin/python3

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
         }

for key in people:
    print("ID:", key)
    for nextkey in people[key]:
        print(nextkey, ":", people[key][nextkey])

'''
for id, dictionary in people.items():
    print("ID:", id)
    for key in dictionary:
        print(key, ":", dictionary[key])
Powyżej mamy drugą metodę na wypisanie kluczy i wartości, ta metoda jest lepsza i tylko można,
zastosować "people,items()" w słownikach.
'''

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
          ]

for dictionery in people2:
    for key in dictionery:
        print(key, ":", dictionery[key])

ratings1 = {
    "Arkadiusz": (2, 1, 2, 3, 2, 3),
    "Agnieszka": (4, 2, 1, 3, 4)
}

# aby wypisać klucze ze słownika
for key in ratings1:
    print(key)
# aby wypisać wartosci kluczy ze słownika
for key in ratings1:
    print(ratings1[key])

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
           ]
