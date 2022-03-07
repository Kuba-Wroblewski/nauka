#!/usr/bin/python3
import time


# napisz program który policzy sume wszystkich liczb od 1 do podanej przez uzytkownika

def sumuj_do(liczba):
    liczbyContener = 0
    for liczby in range(1, liczba + 1):
        liczbyContener += liczby
    return liczbyContener


def sumuj_do2(liczba):
    return sum([
        liczba
        for liczba in range(1, liczba + 1)
    ])


def sumuj_do3(liczba):
    return (1 + liczba) / 2 * liczba


# start = time.perf_counter()
# print(sumuj_do(int(input('\nPrzykład 1,\nPodaj jakąś liczbe dodatnią...'))))
# stop = time.perf_counter()
# print(stop - start)

# start = time.perf_counter()
# print(sumuj_do2(int(input('\nPrzykład 2,\nPodaj jakąś liczbe dodatnią...'))))
# stop = time.perf_counter()
# print(stop - start)

# start = time.perf_counter()
# print(sumuj_do3(int(input('\nPrzykład 3,\nPodaj jakąś liczbe dodatnią...'))))
# stop = time.perf_counter()
# print(stop - start)

def function_performance(func, arg, how_many_times=1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        stop = time.perf_counter()
        sum += stop - start
    return sum


def show_mesage(liczba):
    contener = 0
    for liczba in range(1, liczba + 1):
        contener += liczba
    print(contener)


# print(function_performance(show_mesage, 1))

# print(function_performance(sumuj_do, 4999999, 5))
# print(function_performance(sumuj_do2, 4999999, 5))
# print(function_performance(sumuj_do3, 4999999, 5))


def greet(name, message, separator=" "):
    print(message, name, sep=separator)


greet(name='Kuba', message='Witajcie', separator="\n")
greet('Just', 'hello')
