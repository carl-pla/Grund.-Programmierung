#Aufgabe 1:
planet = "Tatooine" 

print(planet[0:4]) #tatoo
print(planet[3:5]) #oo
print(planet[5:9:], "\n") #ine


# Aufgabe2: palindrome 
palindrom = ["Anna", "Otto", "Rentner", "Karlsruhe"]


for wort in palindrom: 
    testwort = wort.lower().replace(" ", "") #alles in Kleinbuchstaben und Leerzeichen entfernen
    if testwort == testwort[::-1]: 
        print(f"{wort} ist ein Palindrom!")
    elif testwort != testwort[::-1]: 
        print(f"{wort} ist kein Palindrom!")
    else: 
        print("Fehler, konnte nicht überprüft werden.")

    