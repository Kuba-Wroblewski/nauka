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
        definicje
        print(definicje,"\n")

    elif (wybor == "2"):
        if definicje.__len__() == 0:
            print("Niestety nie ma żadnych definicji\n")
            x = 1
        else:
            print(definicje)
            print("Mamy",len(definicje),"definicjie")
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