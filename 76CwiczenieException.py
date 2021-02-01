#!/usr/bin/python3

"""
Funkcja która .otwiera, .czyta, i .zamyka plik o który, jej podamy.
Try: próboje wykonać operacje pod nią jeśli wszsytko się zgadza.
Jeśli nie to sprawdza czy bląd nie jest taki jak wypisany w 
Except jeśli tak to wykonuje to co jest zawarte w tej akcji.

"""

def OpenYourFile():
    AnserUser = input("Podaj nazwę pliku, jaki chcesz otworzyć...\n")
    try:
        with open(AnserUser, "r") as file:
            for element in file:
                result = file.read()
                return result
    except FileNotFoundError:
        print("Nie ma takiego pliku:", AnserUser)


print(OpenYourFile())
# imionatest.txt
