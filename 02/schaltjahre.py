aktuelles_jahr = int(input("Geben Sie ein Jahr ein: "))

for i in range(4):
    if (aktuelles_jahr % 4 == 0 and aktuelles_jahr % 100 != 0) or (aktuelles_jahr % 400 == 0):
        print(aktuelles_jahr, "ist ein Schaltjahr.")
    else:
        print(aktuelles_jahr, "ist kein Schaltjahr.")
        
    break
# This program checks if a given year is a leap year or not.