# Ctrl+Klick oder rechte Maustaste: Create Console for Editor => ipykernel auswählen
# Debugger durch Klick auf Bug aktivieren, Breakpoint setzen
# Menü->Run->Run All Code

def square(x):
    return x*2 #Achtung Fehler!

def cube(x):
    return x**3

def shift_by(x,a):
    return x + a


number = float(input("Bitte Zahl eingeben: "))

result = cube( square(number) )

print(f" {number}**6 = {result}")
