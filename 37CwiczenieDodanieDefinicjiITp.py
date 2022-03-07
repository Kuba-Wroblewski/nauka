#!/usr/bin/python3

definicje = {}

menu = ("1: Dodaj definicje \n2: Znajdź definicje \n3: Usuń definicje \n4: Zakończ program\n")
x = 1
while x == 1:
    print(menu)
    wybor = input("Co chcesz zrobić...?\n")

    if (wybor == "1"):
        klucz = input("Podaj klucz (slowo) do zdefiniowania: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("Pomyślnie dodana definicja")
        print(definicje, "\n")

    elif (wybor == "2"):
        if definicje.__len__() == 0:
            print("Niestety nie ma żadnych definicji\n")
            x = 1
        else:
            print(definicje)
            print("Mamy", len(definicje), "definicjie")
            wybor2 = input("Podaj nazwe definicji jakiej szukasz...?\n")
            print(definicje[wybor2])
            if wybor2 in definicje:
                print("Jest ta definicja\n")
    elif (wybor == "3"):
        if definicje.__len__() == 0:
            print("Niestety nie ma żadnych definicji\n")
            x = 1
        else:
            print(definicje)
            wybor3 = input("Proszę wprowaz nazwę definicji jaką chcesz usunąć...?")
            definicje.pop(wybor3)

    elif wybor == "4":
        print("END PROGRAM")
        x = 0
    else:
        print("Podałes coś z poza zakresu\n")

"""
definicje = {}

while(True):

    print("\n1: Dodaj definicje")
    print("2: Usuń definicje")
    print("3: Znajdź definicje")
    print("4: Pokaż wszystkie definicje")
    print("5: Zakończ program")

    wybor = input("\nCo chcesz zrobić ?\n")

    if (wybor == "1"):
        klucz = input("Wprowadz klucz definicji.\n")
        definicja = input("Wprowadz definicjie.\n")
        definicje[klucz] = definicja
    elif (wybor == "2"):
        klucz = input("Wprowadz definicjie którą chcesz usunąć.\n")
        if klucz in definicje:
            del definicje[klucz]
            print("Poprawnie usuneliśmy definicje: ", klucz)
        else:
            print("Podana definicja: ", klucz, "\nNie znajduje się w liscie definicji")
    elif (wybor == "3"):
        klucz = input("Wprowadz definicjie której szukasz.\n")
        if klucz in definicje:
            print(klucz)
        else:
            print("Podana definicja: ", klucz, "\nNie znajduje się w liscie definicji")



    elif (wybor == "4"):
        if len(definicje) == 0:
            print("Nie ma żadnych definicji")
        else:
            print("Oto wszystkie definicje: ", definicje)
    elif (wybor == "5"):
        break
"""

"""
# moj program numer 2
definicje = {}

while True:
    anser = int(input('''\nWybierz co chcesz zrobić z menu...
    1. Dodać nową definicje.
    2. Usunąć dana definicje
    3. Szukać definicje
    4. Pokaz wszystkie definicje 
    5. Exit \n'''))

    if anser == 1:
        nameOfDefinition = input('Proszę podać nazwe swojej definicji...\n')
        definitions = input('\nSwietnie\nTeraz proszę podać swoją definicje...\n')
        definicje.update({nameOfDefinition : definitions})
        print('Twoja definicja to:', definicje)

    elif anser == 2:
        if len(definicje) > 0: 
            delDefiniction = input('\nProszę podać nazwę definicji która chcesz usunąć...\n')
            print('Usuwamy definicje:', delDefiniction, 
                '\nI związaną z nia wartość:\n', definicje[delDefiniction])
            del(definicje[delDefiniction])
        else:
            print('Nie masz żadnych definicji, wybierz inna opcje w menu')

    elif anser == 3:
        if len(definicje) > 0:
            searchDefinition = input('Proszę wprowadzic szukaną definicje...\n')
            if searchDefinition not in definicje:
                print('Szukanej definicji nie ma w definicji, Sprawdz pisownie')
            else:
                print('Wartość szukanej definicji to:\n', definicje[searchDefinition])
        else:
            print('Nie masz żadnych definicji, wybierz inna opcje z menu')

    elif anser == 4:
        if len(definicje) <= 0:
            print('Nie ma żadnej definicji\n', definicje)
        else:
            print(definicje)

    elif anser == 5:
        print('Exit')
        break
"""
