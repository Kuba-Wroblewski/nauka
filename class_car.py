#!/usr/bin/python3

"""
Programowanie proceduralne charakteryzuje się tym że posiadamy niezależne dane, 
niezależne funkcje. pisząć program budujemy pewien algorymt który łączy te dane 
z tymi funkcjami

Classa próbuje ze sobą połączyć dane jak i funkcje które na tych danych mogą być wykonywane
classa określa jakiego rodzaju informacje będziemy przechowywać, np. przechowujemy informacje
o marce o modelu czy lakier jest okej czy auto jest okej. ale classa nie opisuje żadnego 
konkretnego samochodu to tylko jagby formularz do którego wpisujemy konkretne wartości
opisujące konkretne samochody.

W momencie kiedy powstaje już opis konkretnego samochodu to mówimy w oparciu o klase powstaje
instancja tej klassy - czesto mówimy objekt. instancja klassy będzie  pozwalała na odwołanie 
się wszsystkich własiwosci które posiada klassa.

Często też cechy opisywane przez klasse mozna nazywac włąsciwosciami lub atrybutami tej 
klassy, natomiast funkcje które sa przypisane do klassy będziemy nazywać metodami.
"""


class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)

car_01 = {
    'carBrand': 'Seat',
    'carModel': 'Ibiza',
    'carisAirBagOK': 'True',
    'carisPaintingOK': 'True',
    'carisMechanicOK': 'True'
}

car_02 = {
    'carBrand': 'Opel',
    'carModel': 'Corsa',
    'carisAirBagOK': 'True',
    'carisPaintingOK': 'False',
    'carisMechanicOK': 'True'
}
