#!/usr/bin/python3

"""
Lista jest najbardziej elastycznym typem obiektu uporządkowanej kolekcji.
Może zawierać różne typy danych - liczby, łańcuchy znaków, a nawet inne
listy.
Funkcje : []
cmp ( list1 , list2 ) # Porownuje elementy dwoch list
len ( list ) # Zwraca dlugosc listy
max ( list ) # Zwraca element o najwiekszej wartosci
min ( list ) # Zwraca element o najmniejszej wartosci
list ( seq ) # Konwertuje krotke ( tuple ) na liste

Metody :
list.split() # rozdziel po jakims znaku np. spacji
list . append ( obj ) # Dodaje obiekt obj do listy
2
list . count ( obj ) # Zwraca liczbe wystapien obiektu obj w liscie
list . extend ( seq ) # Dodaje zawartosc seq do listy ( np . inna liste
lub krotke )
list . index ( obj ) # Zwraca najnizszy indeks wystapienia obj w liscie
list . insert ( index , obj ) # Wstawia do listy obiekt obj na pozycje
o indeksie index
list . pop ( obj = list [ -1]) # Usuwa i zwraca ostatni obiekt lub obj z listy
list . remove ( obj ) # Usuwa obiekt obj z listy
list . reverse () # Odwraca liste
list . sort ([ func ]) # Sortuje elementy listy , uzywa funkcji porownania ,
jesli jest podana

Krotki (tuple)
Krotka jest ogólnie rzecz biorąc listą, której nie da się zmodyfikować. Obsługują
one dowolne typy danych, zagnieżdżanie i zwykłe operacje na sekwencjach.
>>> T = (1 , 2 , 3 , 4)
>>> len ( T )
>>> 4
Krotki można konkatenować:
>>> T + (5 , 6)
>>> (1 , 2 , 3 , 4 , 5 , 6)
Można też konwertować na listę:
>>> list ( T )
W związku z tym, że krotki są sekwencjami niezmiennymi (lub inaczej
niemodyfikowalnym typem danych), posiadają mniej metod wbudowanych
niż np. listy.
T . index (2) # zwraca indeks pod jakim znajduje sie wartosc 2
T . count (4) # zlicza wystapienia elementu 4 w krotce
W krotkach można zagnieżdżać inne sekwencje.
3
>>> U = (" mielonka " , 32542.33 , (2 ,3 ,4))
>>> U [2][1]
>>> 3
W praktyce krotki są używane rzadziej niż listy. Jednak ich zdecydowaną
zaletą jest ich niezmienność.

Słowniki
Słowniki są bardzo podobne do list, z tą różnicą, że do poszczególnych
elementów dostaje się za pomocą klucza zamiast indeksu. Klucz może być
stringiem lub liczbą.

"""