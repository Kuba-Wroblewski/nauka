#!/usr/bin/python3

imie = "Arkadiusz"
nazwisko = "Włodarczyk"

print(imie + " ", nazwisko)

pelne = imie + " " + nazwisko
print(pelne)

dlugiString = """\nto jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi to
jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi
to jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi"""

dlugiString2 = "\nto jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi to \
        jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi \
        to jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi"

dlugiString3 = '\nto jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi to' \
               ' jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi' \
               ' to jest jakis tekst aby był dlugi to jest jakis tekst aby był dlugi'

print(dlugiString); print(dlugiString2); print(dlugiString3)

'''
długie stringi możemy zapisać na kilka sposobóœ jak sie nie 
mieszczą w jednej lini lub mają sie nie mieścic w jednej lini.
'''

print(imie[0:2]) # wypisuje od pozycji numer 0 do pozycji numer 2 w tym przykłądzie nie wypisze nam litery numer 2
# ponieważ liczenie zaczyna się od 0

imie = "Kuba"

print(imie[0:3])
print(imie[-4:1])