#!/usr/bin/python3

# program do liczenia podatku VAT 23 % od kwoty netto

VAT = 23
VAT2 = 19
#kursPythonStandart = 1250
#kursPythonZawans = 1750
oprogramowanieB = 165
programB = 215



oblicz_VAT2 = (1 + VAT2/100)
oblicz_VAT = (1 + VAT/100)
#PythonStandart = (kursPythonStandart * oblicz_VAT)
#PythonZawans = (kursPythonZawans * oblicz_VAT)
oprogramowanieB = (oprogramowanieB / oblicz_VAT)
programB =  (programB / oblicz_VAT2)
