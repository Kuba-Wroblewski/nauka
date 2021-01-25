#!/usr/bin/python3

"""

W komendzie print linia 9 powstanie błąd i plik nie zrealizuje ani
    nie zapisze po tym błędzie nic.
Stosujemy komende try: aby spróbować wykonać instrukcje oraz komende
finally aby zamknąć ostatecznie nawet po nie udanych wcześniej operacjach na pliku
Np. błędach.

"""

try:
    file = open("plik_testowy", "w")   #UCHWYT HANDLE
    file.write("sample")
    tab = [15, 45]
    print(tab[1])
    file.write("tab[0]")
    print(0/0)
    a = 5
    file.write("\nsample")
    file.write("\nnosz")
    file.close()
finally:
    # file.write("KONIEC")
    file.close()
