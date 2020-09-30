#!/usr/bin/python3

import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

oceny = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

wygenerowana_liczba = [element
                       for element in range(10, 101)
                       if element % 5 == 0
                       if element % 3 != 0]