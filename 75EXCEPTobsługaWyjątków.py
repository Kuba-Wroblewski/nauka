#!/usr/bin/python3

"""
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanatest.txt

1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliu nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
zapsywał nazwiska do pliku nazwiska.txt

[
 ("Arkadiusz", "Włodarczyk"),
 ("Jakis", "Ziom")
]

"""

lista = []
with open("imionatest.txt", "r") as file:
    for element in file:
        lista.append(tuple(element.split()))
# print(lista)

with open("imiona.txt", "w") as file:
    for element in lista:
        file.write(element[0] + "\n")

with open("nazwiska.txt", "w") as file:
    for element in lista:
        if (len(element) == 2):
            file.write(element[1] + "\n")
        else:
            file.write("\n")



