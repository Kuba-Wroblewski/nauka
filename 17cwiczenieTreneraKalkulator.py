#!/usr/bin/python3

wybór = input("Proszę najpierw wybrać jaką operacje na liczbie chcesz zrobić \n+ - dodawanie,\
- - odejmowanie, / - dzielenie, * - mnożenie, ** - potęgowanie, // - dzielenie w dół, % - moduło \n")

a = int(input("Podaj pierwszą liczbę:\n "))
b = int(input("Podaj drugą liczbę:\n "))

if (wybór == "+" ):
    print(a + b)
elif (wybór == "-" ):
    print(a - b)
elif (wybór == "/" ):
    if (b == 0):
        print("Pamiętaj cholero nie dziel przez zero")
    else:
        print(a / b)
elif (wybór == "//" ):
    if (b == 0):
        print("Pamiętaj cholero nie dziel przez zero")
    else:
        print(a // b)
elif (wybór == "%" ):
    print(a & b)
elif (wybór == "**" ):
    print(a ** b)

