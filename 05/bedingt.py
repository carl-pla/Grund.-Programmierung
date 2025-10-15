# Aufgabe 1 Bedingte Ausgaben
"""
 Konstruiert eine Print-Funktion, die eine Ausgabe nur dann vornimmt,
 wenn die test-Funktion als Ergebnis True zurückgibt.

 args:
 test: Eine Funktion, die True oder False zurückgibt.

 return value:
function: Eine Print-Funktion, die eine Nachricht nur dann ausgibt,
 wenn test(Nachricht) True ist.
"""
def conditional_print(test): 
   if test % 2 == 0 and type(int): 
       print("durch 2 teilbar und int")
       return True 
   
   elif test % 2 != 0 and type(int): 
    print("Die Zahl ist nicht nur 2 teilbar")
    return False
    
   elif test != type(int): 
    print("Du musst einen int-Zahlenwert eingeben")
    return False
 
print(conditional_print(test=5))
   
   