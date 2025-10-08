x1 = 10**20
x2 = 1223.0
x3 = 10**18
x4 = 10**15
x5 = 3.0
x6 = -10**12

y1 = 10**20
y2 = 2.0
y3 = -10**22
y4 = 10**13
y5 = 2111.0
y6 = 10**16

print(x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5 + x6*y6)#Ergebnis laut Python: 0.0

"""
Computer speichern Fließkommazahlen nach dem IEEE 754-Standard.
    Das bedeutet:
        Eine Zahl besteht aus Sign, Exponent und Mantisse (z. B. bei float: 64 Bit)
        Nur endliche viele Brüche können exakt dargestellt werden
        Viele Dezimalbrüche (z. B. 0.1) sind unendlich lang im Binärsystem → also wird gerundet
"""

#LÖSUNG MIT DEM DECIMAL-MODUL
from decimal import Decimal, getcontext

getcontext().prec = 50  # Präzision erhöhen

x1 = Decimal(10)**20
x2 = Decimal(1223.0)
x3 = Decimal(10)**18
x4 = Decimal(10)**15
x5 = Decimal(3.0)
x6 = Decimal(-10)**12

y1 = Decimal(10)**20
y2 = Decimal(2.0)
y3 = Decimal(-10)**22
y4 = Decimal(10)**13
y5 = Decimal(2111.0)
y6 = Decimal(10)**16

result = x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5 + x6*y6
print(round(x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5 + x6*y6, 1)) #Ergebnis laut Python: 2111000000000000.0

