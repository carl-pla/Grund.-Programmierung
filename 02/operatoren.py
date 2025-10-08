#Aufgabe 2 
def Assignment():
    a = input("Geben Sie ihren Namen ein: ")
    b = input("Geben Sie ihren Vornamen ein: ")
    
    a,b = b, a 
    print(a, b)
    

#Aufgabe 1 a) +b)
def tf(): 
    # Eingabe von zwei Wahrheitswerten (t/f)
    eingabe1 = input("Geben Sie True oder False ein 1 (t/f): ").lower()
    eingabe2 = input("Geben Sie True oder False ein 2 (t/f): ").lower()
    operator = input("Geben Sie den Operator ein (and/or/not): ").lower()

    # Eingaben in echte boolesche Werte umwandeln
    if eingabe1 == "t":
        val1 = True
    elif eingabe1 == "f":
        val1 = False
    else:
        print("Ungültige Eingabe bei Wert 1.")
        return

    if eingabe2 == "t":
        val2 = True
    elif eingabe2 == "f":
        val2 = False
    else:
        print("Ungültige Eingabe bei Wert 2.")
        return

    # UND-Operation (and)
    if operator == "and":
        ergebnis = val1 and val2
        print("Ergebnis: ", ergebnis)
    #or opearation
    elif operator == "or":
        ergebnis = val1 or val2
        print("Ergebnis: ", ergebnis)
    #not operation
    elif operator == "not":
        ergebnis = not val1
        print("Ergebnis:", ergebnis)
        ergebnis = not val2
        print("Ergebnis: ", ergebnis)
    else:
        print("Ungültiger Operator.")
tf()

#Aufgabe 1 c)
print(True and False or False)
print((True and False) or False)
print(True and (False or False))