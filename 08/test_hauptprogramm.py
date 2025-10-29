import math
import hauptprogramm as hp

# Wir definieren eine Funktion, die die get_radius Funktion im Test ersetzen soll
def double_get_radius():
    return 5

def test_circle_area():
    # Funktion get_radius wird durch double ersetzt
    # (dependency injection)
    hp.get_radius = double_get_radius 
    area = hp.circle_area()
    if area != 25*math.pi:
        print(f"Unerwarteter Flächeninhalt {area} für Radius 5")
        
test_circle_area()



