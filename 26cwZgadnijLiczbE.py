#!/usr/bin/python3

szukanaLiczba = 50
print("Witaj")
print("Myśle o pewnej liczbie całkowitej, spróbuj \
odgadnąć jaka to liczba")
while (szukanaLiczba != 49):
    x = int(input("Podaj liczbę: "))
    if (x > 50):
        print("Poda liczba jest za duża, spróbuj jeszcze raz")
    elif (x < 50):
        print("Podana liczba jest za mała, spróbuj jeszcze raz")
    else:
        print("Brawo nasza liczba to:",szukanaLiczba)
        break


"""
# Przykłąd zrobiony przez trenera

szukanaliczba = 50
zgadywanaliczba = 0
while zgadywanaliczba != szukanaliczba:
    zgadywanaliczba = int(input("Odgadnij liczbe: "))

    if (zgadywanaliczba == szukanaliczba):
        print("Brawo")
    else:
        print("spróbuj jeszcze raz")
"""
