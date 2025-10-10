# Aufgabe 3: Iteration

for zaehlen in range(1, 100): 
    if zaehlen % 3 == 0 and zaehlen % 5 == 0: 
        wort = "R2D2"
        print(wort)
    elif zaehlen % 5 == 0: 
        wort = "D2"
        print(wort)
    elif zaehlen % 3 == 0:
        wort = "R2"
        print(wort)
    else: 
        print(zaehlen)