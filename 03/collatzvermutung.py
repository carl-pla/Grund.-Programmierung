# Aufgabe 5: Collatz-Vermutung
import random as rd
zahl = 0

for i in range(30):
    zahl = rd.randint(1, 10)
    check = False
    
    if zahl % 2 == 0:
        ergebnis = zahl / 2 
        print(f"Die Zahl ist: {zahl}, das Ergebnis ist: {ergebnis}")
        if ergebnis == 1:
            check = True
            print("\n Die Collatz-Vermutung ist erfüllt.")
            break
        
    elif zahl % 2 != 0: 
        ergebnis = (3*ergebnis) + 1
        print(f"Die Zahl ist: {zahl}, das Ergebnis ist: {ergebnis}")
        if ergebnis == 1:
            check = True
            print("Die Collatz-Vermutung ist erfüllt.")
            break
    
    else: 
        print("Fehler, ungültige Zahl.")