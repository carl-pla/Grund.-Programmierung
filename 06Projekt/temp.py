# Aufgabe: Baue einen Tempertaur-Umrechner 


#Einleitung, um den User zu begrüßen und ihm mitteilen welche Syntax für die Konvertierung nötig ist 
einleitung = "Willkommen zum Temperatureinheiten-Umrechner! \nSie können hier Temperaturen zwischen Celsius(c), Kelvin(k) und Fahrenheit(f) umrechnen."
print(einleitung)

# Hauptfunktion umzurechnen 
def umrechnen():
    
    
    #Eingabe überprüft, ob float eingegebn wird, wenn nicht wird wiederholt
    eingabe_wert = input("\nWelcher Wert soll umgewandelt werden?: ")
    try: 
        eingabe_wert = float(eingabe_wert) 
    except:
        print("Du darfst nur Integer oder Floats verwenden")
        return umrechnen()
   
    
    #3 Eingabewerte: Wert, Starteinheit, Zieleinheit
    eingabe_einheit_start = input("Welche Einheit benutzen Sie? (C/K/F): ")
    eingabe_einheit_start = eingabe_einheit_start.upper() #Großschreibfehler vermeiden
    eingabe_einheit_ziel = input(f"In welche Einheit soll '{eingabe_einheit_start}' umgerechnet werden? (C/K/F): ")
    eingabe_einheit_ziel = eingabe_einheit_ziel.upper() #Großschreibfehler vermeiden
   
    # Einzelnen Umrechnungen
    if eingabe_einheit_start == "C" and eingabe_einheit_ziel == "K": 
            ergebnis = 273.15 + eingabe_wert
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
            
    elif eingabe_einheit_start == "C" and eingabe_einheit_ziel == "F": 
            ergebnis = (9/5) * eingabe_wert
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
        
    elif eingabe_einheit_start == "K" and eingabe_einheit_ziel == "F": #round fehler
            ergebnis = 1.8 * ((eingabe_wert) - 273) + 32
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
         
    elif eingabe_einheit_start == "K" and eingabe_einheit_ziel == "C": 
            ergebnis = -273.15 + eingabe_wert 
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
            

    elif eingabe_einheit_start == "F" and eingabe_einheit_ziel == "C": 
            ergebnis = (5/9) * (eingabe_wert) - 32
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
           

    elif eingabe_einheit_start == "F" and eingabe_einheit_ziel == "K": 
            ergebnis = ((eingabe_wert) - 32) * (5/9) + 273,15 
            print(f"Dein Zielwert beträgt: {round(ergebnis, 2)}{eingabe_einheit_ziel}") 
            wiederholen()
            
        
    #Fehlernetz: Selbe Einheit, falsche Einheit
    elif eingabe_einheit_start == eingabe_einheit_ziel: 
        print("Du darfst nicht die selbe Einheit benutzen!")
        wiederholen()
        
    elif eingabe_einheit_start or eingabe_einheit_ziel != "F" "C" "K":
        print("Du kannst nur in Celsius(C), Kelvin(K), Fahrenheit(F) umrechnen!")
        wiederholen()
    

 
# Wiederholungsfrage, um Programm unendlich viele User Inputs entgegenzunehmen 
def wiederholen(): 
        wiederholen = input("\nSoll das folgende Programm wiederholt werden?(y/n): ") #Wiederholungsfunktion
        print(wiederholen)
            
        if wiederholen == "y": 
            umrechnen()
             
            
        elif wiederholen == "n":
            print("Vielen Dank für die Nutzung!")
            
        else: 
            print("Eingabe war ungültig, nochmal: ")

#Abfrage der Funktionen, dass das Programm ausgegeben werden kann
umrechnen()
wiederholen()



        
    
    
   
   
