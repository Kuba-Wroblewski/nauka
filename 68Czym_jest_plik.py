#!/usr/bin/python3
"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku.

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO

Operacje na plikach
1) otwieranie
2) pisanie/czytanie
3) zamykanie

podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie, jeśli nie to stworzy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy
             rozpoznawały plik w odpowiedni dla tych programów sposób

Musimy zamykać każdy plik żeby doszło do zmian i zwolnić pamięć !     
klikając na plik 2 razy zostaje uruchomiony plik i akcja która jest w nim zawarta.
"""

a = 5

file = open("plik_testowy", "w")   #UCHWYT HANDLE
file.write("sample\n")
print(0/0)
file.write("sample")
file.close()

file = open("plik_testowy2.txt", "w")   #UCHWYT HANDLE
file.write("sample.2\n")
file.write("sample.2")
file.close()  


