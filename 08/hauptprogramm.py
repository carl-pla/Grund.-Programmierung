import math

def get_radius():
    return float(input("Bitte Radius eingeben: "))

def circle_area():
    radius = get_radius()
    return (radius*2)*math.pi  #absichtlicher Fehler, um Test zu erläutern 

if __name__ == "__main__":
    print(f"Kreisfläche = {circle_area()}")
