light_side = ["Luke", "Leia", "Yoda"]
favourite_characters = light_side

copy1 = light_side.copy() 

""" 
a) unterschiedliche Objektaufgerufen: 
Man prüft die Variablen gegeneinander, ob diese den selben Inhalt haben
"""

if id(copy1) == id(light_side): 
    print("1.Fall Selbes Objekt")
    #print(copy1)
else:
    print("1.Fall Unterschiedliche Objekte")



#b)
helle_seite = ["Luke", "Leia", "Yoda"]
dunkle_seite = ["Darth Vader", "Darth Sidious"]

star_wars = [helle_seite,dunkle_seite]

copy2 = star_wars.copy()

"""
Die Objekte werden anhand der ID erkannt, ob es diese nur einmalig gibt
"""
if id(copy2) == id(star_wars): 
    print("2.Fall Selbes Objekt")
    #print(copy2)
else:
    print("2.Fall Unterschiedliche Objekte")

"""
Jetzt werden die einzelnen Elemente der Listen geprüft,
ob diese Objekte die selben Elemente haben
"""
if copy2[0:2] == star_wars[0:2]: 
    print(" \nDas erste und zweite Objekt haben die selben Elemente")
else: 
    print("Nicht die selben Elemente")