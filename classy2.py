#!/usr/bin/python3

class Person():

    def __init__(self, name):
        self.name = name
        self.nazwisko = 'Kwiatkowski'
        self.age = 25

class Employee(Person):

    def __init__(self, position):
        super().__init__('Tomek')
        self.posiotion = position
        self.specjalization = 'Python'

class Client(Person):

    def __init__(self, name):
        super().__init__(name)
        self.ordered = 'Website'


pracownik = Employee('Programer')
print(pracownik.name)
print(pracownik.posiotion)

pracownik2 = Employee('Designer')
print(pracownik2.name)
print(pracownik2.posiotion)

klient = Client('Marta')
print(klient.name)
print(klient.ordered)

klient2 = Client('Weronika')
print(klient2.name)
print(klient2.ordered)


