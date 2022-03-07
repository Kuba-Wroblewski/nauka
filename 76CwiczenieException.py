#!/usr/bin/python3

"""
Funkcja która .otwiera, .czyta, i .zamyka plik, który, jej podamy.
Try: próboje wykonać operacje pod nią jeśli wszsytko się zgadza.
Jeśli nie to sprawdza czy bląd nie jest taki jak wypisany w 
Except jeśli tak to wykonuje to co jest zawarte w tej akcji.

"""


# 1 możliwkość wykonania.
def OpenYourFile():
    anser_user = input("Podaj nazwę pliku, jaki chcesz otworzyć...\n")
    try:
        with open(anser_user, "r") as file:
            for element in file:
                result = file.read()
                return result
    except FileNotFoundError:
        print("Nie ma takiego pliku:", anser_user)


print(OpenYourFile())
# imionatest.txt

# 2 możliwość wykonania.
# anser_user = input("Please tab name of file to open\n")
# try:
#     with open(anser_user, "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
