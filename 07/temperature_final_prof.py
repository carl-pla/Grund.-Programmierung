"""
Zunächst: 
    - Konstanten und Funktionen
    - Diese könnten auch in anderen Programmen nützlich sein
    - unit = Einheit
"""
MIN_KELVIN = 0
MIN_CELSIUS = -273.15
MIN_FAHRENHEIT = -459.67

def is_temperature_valid(degree, unit):

    if unit == "K" and degree < MIN_KELVIN:
        is_valid = False
        error_text = f"\nTemperaturen kleiner {MIN_KELVIN} K sind nicht möglich\n"
    elif unit == "C" and degree < MIN_CELSIUS:
        is_valid = False
        error_text = f"\nTemperaturen kleiner {MIN_CELSIUS} C sind nicht möglich\n"
    elif unit == "F" and degree < MIN_FAHRENHEIT:
        is_valid = False
        error_text = f"\nTemperaturen kleiner {MIN_FAHRENHEIT} F sind nicht möglich\n"
    else:
        is_valid = True
        error_text = ""
        
    return is_valid, error_text

def is_unit_correct(unit):
    if unit in ("C","F","K"): # Celsius, Fahrenheit, Kelvin 
        error_text = ""
        is_correct = True
    else:
        error_text = f"\nEingegebene Einheit {unit} ist nicht zulässig\n"
        is_correct = False

    return is_correct, error_text

def celsius_to_kelvin(degree):
    return degree + 273.15

def kelvin_to_celsius(degree):
    return degree - 273.15 # vorheriger Fehler 

def kelvin_to_fahrenheit(degree):
    return 1.8*(degree - 273.15) + 32 

def fahrenheit_to_kelvin(degree):
    return (degree - 32)/1.8 + 273.15 
    
def convert_temperature(start_unit, target_unit, degree):
    if start_unit == "C" and target_unit == "K":
        result = celsius_to_kelvin(degree)
    elif start_unit == "K" and target_unit == "C":
        result = kelvin_to_celsius(degree)
    elif start_unit == "C" and target_unit == "F":
        result = kelvin_to_fahrenheit( celsius_to_kelvin(degree) )
    elif start_unit == "F" and target_unit == "C":
        result = kelvin_to_celsius( fahrenheit_to_kelvin(degree) )
    elif start_unit == "K" and target_unit == "F":
        result = kelvin_to_fahrenheit(degree)
    elif start_unit == "F" and target_unit == "K":
        result = fahrenheit_to_kelvin(degree)
    elif start_unit == target_unit:
        result = degree
    else:
        print("Noch nicht implementiert")

    return result
    
"""
Hier beginnt die Implementierung des CLI (Command Line Interface), 
d.h. das Handling von User-Input 
"""
def main():
    
    while True:
        start_unit = input(
                       "Konvertierung einer Temperatur in eine andere Einheit. \n" \
                       "Ausgangseinheit (C)elsius, (K)elvin, (F)ahrenheit: " 
        )
        is_correct, error_text = is_unit_correct(start_unit)
        if is_correct == True:
            break
        else:
            print(error_text)

    while True:
        target_unit = input("Zieleinheit (C)elsius, (K)elvin, (F)ahrenheit: ")
        is_correct, error_text = is_unit_correct(target_unit)
        if is_correct == True:
            break
        else:
            print(error_text)
        
    while True:
        try:
            degree = float(
                       input(
                         f"Wie hoch ist die Temperatur in der Ausgangseinheit {start_unit}? \n"\
                         "Eingabe: "
            ))
            is_valid, error_text = is_temperature_valid(degree,start_unit)
            if is_valid == False:
                print(error_text)
            else:
                break
        except ValueError:
            print("\nBitte eine Zahl eingeben!\n")
    
    print(f"\nDie Temperatur beträgt {convert_temperature(start_unit,target_unit,degree)} {target_unit}.") 


if __name__ == "__main__":
    main()
