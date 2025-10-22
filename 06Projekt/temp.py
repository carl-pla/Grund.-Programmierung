# Aufgabe: Baue einen Tempertaur-Umrechner 

#Global definierte Variablen, sodass auch außerhalb der FUnktion draufzugegriffen werden kann
k = 0
c = 0
f = 0

einleitung = "Willkommen zum Temperatureinheiten-Umrechner! \n Sie können hier Temperaturen zwischen Celsius(c), Kelvin(k) und Fahrenheit(f) umrechnen."
print(einleitung)

eingabe_wert = int(input("Welcher Wert soll umgewandelt weden?"))
eingabe_einheit_start = input("Welche Einheit benutzen sie? (c/k/f): ")
eingabe_einheit_ziel = input(f"In welche Einheit soll {eingabe_einheit_start }umgerechnet werden? (c/k/f): ")


while True: 
    def umrechnen():
        if eingabe_einheit_start == c and eingabe_einheit_ziel == k: 
            ergebnis = k = 273.15 + c
            print(ergebnis)
        elif eingabe_einheit_start == c and eingabe_einheit_ziel == f: 
            ergebnis = f = (9/5) * c + 32
            print(ergebnis)
    
        elif eingabe_einheit_start == k and eingabe_einheit_ziel == f: 
            ergebnis = f = 	(k - 273,15) * 5/9 
            print(ergebnis)
       
        elif eingabe_einheit_start == k and eingabe_einheit_ziel == c: 
            ergebnis = c = -273.15 + k 
            print(ergebnis)

        elif eingabe_einheit_start == f and eingabe_einheit_ziel == c: 
            ergebnis = c = (5/9) * (f - 32)
            print(ergebnis)

        elif eingabe_einheit_start == f and eingabe_einheit_ziel == k: 
            ergebnis = k = (f - 32) * 5/9 + 273,15 
            print(ergebnis)
        
        #Fehlernetz
        else: 
            print("Die Eingabe war ungültig!")
            wiederholen = input("Soll das folgende Programm wiederholt werden?(y/n): ") #Wiederholungsfunktion
            print(wiederholen)
        
            if wiederholen == "y": 
                continue
            elif wiederholen == "n":
                print("Vielen Dank für die Nutzung!")
                break
            else: 
                print("Eingabe war ungültig, nochmal: ")
                continue
            
    