#!/usr/bin/python3

"""
podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie, jeśli nie to stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania, nie usunie pliku jesli taki istnieje

w+ - do pisania i czytania, różni się tym, że usunie zawartość pliku lub stworzy nowy jeśli go nie było

a+ - "wieczny tryb" dopisywania i przy okazji czytania UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istaniał stworzy go. Wiec jak chcesz go przeczytac postaw sie na pocztek funkcja "seek"

"""


with open("plik_testowy2", "a+") as file:
   file.write("Tak")
   file.seek(0)
   print(file.readline())
   print(file.tell())
   file.write("[Go, Go, niet]")
