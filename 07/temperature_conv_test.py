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
        "X": False,
        (3.4): None, 
        -345: False
        
       # hier wird geprüft, ob die Eingabe den gewünschten Wert zurückgibt 
    }
    
#Testfunktion: is_temperature_valid
def is_temperature_valid(): 
    test_data = testdaten()
    for x, expected_values in test_data.items(): 
        temp_valid = tf.is_temperature_valid(x)
        if temp_valid != expected_values: 
            print(f"Funktion is_temperature_valid: Ergebnis von {x} ist {expected_values}")  
    

#Testfunktion: is_unit_correct
def is_unit_correct(): 
    test_data = testdaten()
    for x, expected_values in test_data.items(): 
        unit_cor = tf.is_unit_correct(x)
        if unit_cor != expected_values: 
            print(f"Funktion is_unit_correct: Ergebnis von {x} ist {expected_values}")

#Testfunktion: convert_temperature
def convert_temperature(): 
    test_data = testdaten()
    for x, expected_values in test_data.items():
        con_temp = tf.is_unit_correct(x)
        if con_temp != expected_values: 
            print(f"\nFunktion convert_temperature: Ergebnis von {x} ist {expected_values}")

if __name__ == "__main__":
    is_temperature_valid()
    is_unit_correct()
    convert_temperature()
    
    
