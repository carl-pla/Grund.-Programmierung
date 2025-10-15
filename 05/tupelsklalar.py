# Aufgabe 2: Skalar Multiplkation 
s = 4
x = (1, 2.2, 3)


def scalar_multiplikation(s, x): 
    """
 Berechnet das Ergebnis der skalaren Multiplikation von s und x.

 args:
 s
 x
Objekt vom Typ int oder float
Tupel mit Komponenten, die Objekte vom Typ int oder float sein dürfen

return value
Ergebnis der skalaren Multiplikation von s und x, Objekttyp tuple
 """
    ergebnis = tuple(s * element for element in x)
    return ergebnis

result = scalar_multiplikation(s, x)
print(result)