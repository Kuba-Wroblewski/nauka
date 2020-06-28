#!/usr/bin/python3

import math

while True:
    print("\n1 - Oblicz pole kwadratu")
    print("2 - Oblicz pole prostokątu")
    print("3 - Oblicz pole kola")
    print("4 - Oblicz pole trapezu")
    print("5 - Koniec programu")

    odpowiedz = input("\nCo chcesz zrobic...?\n")

    def pole_kwadratu(a):
        return a * a

    def pole_prostokata(a, b):
        return a * b

    def pole_kola(r):
        return math.pi * r ** 2

    def pole_trojkata(a, h):
        return 0.5 * a * h

    def pole_trapezu(a, b, h):
        return (a + b) / 2 * h

    if odpowiedz == "1":
        a = int(input("Prosze podać długość jednego z boków kwadratu\n"))
        print("Pole kwadratu wynosi", pole_kwadratu(a))

    elif odpowiedz == "2":
        a = int(input("Prosze podać długość jednego z boków prostokąta\n"))
        b = int(input("Prosze podać długość drugiego z boków prostokąta\n"))
        print("Pole prostokąta wynosi", pole_prostokata(a, b))

    elif odpowiedz == "3":
        r = int(input("Prosze podać promień koła\n"))
        print("Pole koła wynosi", pole_kola(r))

    elif odpowiedz == "4":
        a = int(input("Prosze podać długość jednego z boków trapezu\n"))
        b = int(input("Prosze podać długość drugiego z boków trapeza\n"))
        h = int(input("Prosze podać wysokość trapezu\n"))
        print("Pole trapezu wynosi", pole_trapezu(a, b, h))

    elif odpowiedz == "5":
        break

    else:
        print("Podałeś błędny parametr z zakresu")
