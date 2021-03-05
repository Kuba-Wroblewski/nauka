#!/usr/bin/python3

class Car():
    def __init__(self, marka):
        self.marka = marka

    def info(self):
        print("Marka:", self.marka)


first_car = Car("Skoda")
second_car = Car("Opel")

first_car.info()
second_car.info()
