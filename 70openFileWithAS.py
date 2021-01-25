#!/usr/bin/python3

"""

with ... as ...

podajemy jaki plik w jakim trybie gdzie go zapisujemy,
A nastepnie wykonujemy operacje jak operacje zostaną wykonane automatycznie zostanie zamknięty
nawet jak po drodze zostanie wykonana jakaś operacja wyjątkowa ( błąd ).

"""


with open("plik_testowy.txt", "w") as file: #UCHWYT HANDLE
    file.write("sample\n")
    # print(0/0)
    a = 5
    file.write("sample")