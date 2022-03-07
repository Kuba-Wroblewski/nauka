#!/usr/bin/python3

"""

JSON - to format danych, który posiada wspólne reguły zapisu danych dla wszystkich języków programowania.
Dzięki czemu dane raz zapisane w formacie JSON mogą być odczytane przez każdego programistę nawet jeśli programuje w innym języku programowania.

json.dumps - zapisuje dane do postaci Stringowej json
json.dump - zapisuje dane do pliku w postaci json
ensure_ascii=False (or True) - False pokazuje polskie znaki w pliku json True (domyślnie) nie pokazuje

"""

import json

imiona = ["""
Arkadiusz Włodarczyk,
Meadow,
Carla Baker,
Lily-May Rosas,
Inez Emerson,
Stuart Harrington,
Lemar Calderon,
Zahraa Joyner,
Niam Martin,
Ezmae Hull,
Athena Frost,
Arkadiusz Marx"""]

# Zapisuje do JSON  w postaci stringowej
encodeImiona = json.dumps(imiona)
print(encodeImiona)

# zapisuje dane do pliku w postaci JSON
with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(imiona, file, ensure_ascii=False)
