#!/usr/bin/python3

"""
JSON
JSON - to format danych, który posiada wspólne reguły zapisu danych dla wszystkich języków programowania.
Dzięki czemu dane raz zapisane w formacie JSON mogą być odczytane przez każdego programistę nawet jeśli programuje w innym języku programowania.


"""

import json

imiona = ["""
Arkadiusz Włodarczyk
Meadow
Carla Baker
Lily-May Rosas
Inez Emerson
Stuart Harrington
Lemar Calderon
Zahraa Joyner
Niam Martin
Ezmae Hull
Athena Frost
ArkadiuszMarx"""
]

print(json.dumps(imiona))

