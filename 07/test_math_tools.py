import math_tools as mt 

# Testdaten
def fehler():
    return {
        # key = Eingabe, value = erwarteter Wert
        -2:4,
        -1:1,
         0:0,
         1:1,
         3:9,
        -7:49,
         9:81
    }

# Testfunktion
def test_square():
    test_data = fehler()
    for x, expected_value in test_data.items():
        square_x = mt.square(x)
        if square_x != expected_value:
            print(f"Funktion square: Ergebnis von square({x}) ist {square_x} und nicht der erwartete Wert {expected_value}")

if __name__ == "__main__":
    test_square()


