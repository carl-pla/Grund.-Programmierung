# Aufgabe 1 Bedingte Ausgaben
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
   
   