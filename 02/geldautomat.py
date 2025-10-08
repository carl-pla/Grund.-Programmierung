#personal information 
pin = "2345"
kontostand = 2300
abheben = 0

anmelden = input("Bitte geben Sie Ihre PIN ein: ")
for i in range(5): 
    if anmelden == pin:
        print("Anmeldung erfolgreich!")
        print("Ihr Kontostand beträgt: ", kontostand, "Euro")
    else: 
        print("Falsche PIN. Anmeldung fehlgeschlagen (4-stelliger Code).")
        break
    
    abheben = int(input("Wie viel Geld möchten Sie abheben?: "))
    
    if abheben > kontostand:
        print("Ihr Kontostand ist nicht ausreichend für diese Abhebung.")
    else: 
        print("Abhebung erfolgreich!")
    kontostand -= abheben 
        
    print("Ihr neuer Kontostand beträgt: ", kontostand, "Euro")
    wiederholen = input("Möchten Sie eine weitere Transaktion durchführen? (j/n): ").lower()
    
    if wiederholen != 'j':
        print("Vielen Dank für die Nutzung unseres Geldautomaten. Auf Wiedersehen!")
        break