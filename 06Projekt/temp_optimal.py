# Temperatur-Umrechner
# Unterstützt: Celsius (C), Kelvin (K), Fahrenheit (F)

"""
Struktur Tipps: 
-Methoden für möglichst alles benutzen 
-Hauptfunktion: Try&Except, Erlaubte Werte/Einheiten abfragen 
-Umrechnungen 
-Ausgabe
-Wiederholungsfunktion 
-Programmstart __main__ 

"""

def begruessung():
    print("Willkommen zum Temperatureinheiten-Umrechner!")
    print("Sie können hier Temperaturen zwischen Celsius (C), Kelvin (K) und Fahrenheit (F) umrechnen.")
    print("-" * 60) #optische Zeilentrennung 


def umrechnen():
    # Eingabewert abfragen und prüfen
    while True:
        try:
            wert = float(input("\nGeben Sie den Temperaturwert ein: "))
            break
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")

    # Einheiten abfragen
    start = input("Aus welcher Einheit? (C/K/F): ").strip().upper()
    ziel = input("In welche Einheit soll umgerechnet werden? (C/K/F): ").strip().upper()

    # Eingaben prüfen
    erlaubte = ["C", "K", "F"]

    if start not in erlaubte or ziel not in erlaubte:
        print("Nur 'C', 'K' oder 'F' sind erlaubt!")
        return umrechnen()

    if start == ziel:
        print("Starteinheit und Zieleinheit dürfen nicht gleich sein!")
        return umrechnen()

    # Umrechnung durchführen
    ergebnis = None

    # Celsius → ...
    if start == "C" and ziel == "K":
        ergebnis = wert + 273.15
    elif start == "C" and ziel == "F":
        ergebnis = (wert * 9/5) + 32

    # Kelvin → ...
    elif start == "K" and ziel == "C":
        ergebnis = wert - 273.15
    elif start == "K" and ziel == "F":
        ergebnis = (wert - 273.15) * 9/5 + 32

    # Fahrenheit → ...
    elif start == "F" and ziel == "C":
        ergebnis = (wert - 32) * 5/9
    elif start == "F" and ziel == "K":
        ergebnis = (wert - 32) * 5/9 + 273.15

    # Ausgabe
    print(f"\n {wert}{start} entsprechen {round(ergebnis, 2)}{ziel}")

    wiederholen()


def wiederholen():
    antwort = input("\nMöchten Sie eine weitere Umrechnung durchführen? (y/n): ").strip().lower()
    if antwort == "y":
        umrechnen()
    elif antwort == "n":
        print("\n Vielen Dank für die Nutzung des Umrechners!")
    else:
        print("Ungültige Eingabe. Bitte 'y' oder 'n' eingeben.")
        wiederholen()


# Programmstart
if __name__ == "__main__":
    begruessung()
    umrechnen()
