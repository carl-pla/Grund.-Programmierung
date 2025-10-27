import temperature_final_prof as tf

"""
Inputs können noch nicht automatisiert getestet werden, müssen manuell geprüft werden!
"""


absolute_0_f = tf.kelvin_to_fahrenheit(0) #muss sein wegen name_clashes (variablen/funktionen können überschneiden)

#Testdaten
def testdaten(): 
    return {
        "C" : True, 
        "F": True,
        "K": True,
        (3.4): None, 
        
       # hier wird geprüft, ob die Eingabe den gewünschten Wert zurückgibt 
    }
    
#Testfunktion: is_unit_correct
def is_unit_correct(): 
    test_data = testdaten()
    for x, expected_values in test_data.items(): 
        temp_valid = tf.is_unit_correct(x)
        if temp_valid != expected_values: 
            print(f"Funktion is_unit_correct: Ergebnis von {x} ist {expected_values}")

#Testfunktion: convert_temperature
def convert_temperature(): 
    test_data = testdaten()
    for x, expected_values in test_data.items():
        temp_valid = tf.is_unit_correct(x)
        if temp_valid != expected_values: 
            print(f"\nFunktion convert_temperature: Ergebnis von {x} ist {expected_values}")

if __name__ == "__main__":
    is_unit_correct()
    convert_temperature()
    
    
