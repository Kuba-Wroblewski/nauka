#!/usr/bin/python3

"""
    Argumenty kluczowe i pozycyjne
    kluczowy - w postaci: klucz - wartość (domyślna)
    pozycje - takich, których liczy się kolejność przy wywołaniu
"""


def greet(name, message, separator=" "):
    print(message, name, sep=separator)


greet("Arek", "Witajcie", "\n")
