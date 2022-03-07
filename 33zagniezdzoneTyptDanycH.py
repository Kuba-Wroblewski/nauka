#!/usr/bin/python3

# TYPY ZAGNIEŻDZONE umożliwi nam to zebranie danych np. listy krotki itp. w liste lub krotke itp.

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 35
plec2 = "kobieta"

osoba1 = ("Arkadiusz", 29, "mężczyzna")
osoba2 = ("Wioletta", 35, "kobieta")
osoba3 = ("Kuba", 33, "mężczyzna")

listaGosci = [
    ("Arkadiusz", 28, "mężczyzna"),
    ("Wioletta", 35, "kobieta"),
    ("Kuba", 33, "mężczyzna")
]

print(listaGosci[0])
listaGosci.append(("Karol", 30, "mężczyzna"))
print(listaGosci)
print(listaGosci[3])

listaGosci = {
    ("Arkadiusz", 28, "mężczyzna", 687489987),
    ("Wioletta", 35, "kobieta", 698136203),
    ("Kuba", 33, "mężczyzna",608136023)
}
listaGosci2 = {
    ("Arkadiusz", 28, "mężczyzna",687489987),
    ("Wiola", 44, "kobieta",2344324),
    ("Franek", 21, "mężczyzna",324324324)
}
listaGosci.add(("Piotr", 35, "mężczyzna", 3456465484))

print(listaGosci & listaGosci2) # pokazało nam jaki element sie powtarza
print(listaGosci | listaGosci2) # zsumowało listy gosci ale bez powtórzeń
for imie, wiek, plec, tel in listaGosci:
    print("Imię: ", imie)
    print("wiek: ", wiek)
    print("płeć: ", plec)
    print("tel: ", tel)
    print("\n")