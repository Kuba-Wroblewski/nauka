#!/usr/bin/python3

"""
Korzystając z - with ... as ...
Aby sczytać z pliku zawartość poprzez "file.read()" zapisujemy tą funkcje pod jakąś zmienną.
Ponieważ plik sczytany będzie własnie pod tą funkcją.
Jak po odczytaniu znaki polskie nie będą poprawnei szczytane, to dodajemy "encoding=UTF-8" ( kodowanei znaków )
można sprawdzic encoding linia 17
Jak chcemy aby odrazy szczytane informacje były zapisane w liscie to używamy funkcji ".splitlines()"


file.read()             - czyta cały plik zachowuje "\n" 
file.read().splitlines  - czyta cały plik, wrzuca w liste bez "\n"
file.readline()         - czyta jedną linie z pliku, gdy dodamy kilka redline każda będzie poprzedzona odstępem
file.readlines()        - czyta wszsytkie linie, odrazu wrzuci wszystko w liste i zachowa "\n"
sam print podobno dodaje od siebie jeden enter
"""

# UCHWYT ZAPISUJEMY PLIK ABY MOZNA BYLO SIE DO NIEGO PÓŹNIEJ ODWOŁAĆ
with open("plik_testowy", "r", encoding="UTF-8") as file:
    imiona = file.read().splitlines()

print(imiona)
# print(imiona[2])
print(file.encoding, "\n")

# UCHWYT ZAPISUJEMY PLIK ABY MOZNA BYLO SIE DO NIEGO PÓŹNIEJ ODWOŁAĆ
with open("plik_testowy", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)
