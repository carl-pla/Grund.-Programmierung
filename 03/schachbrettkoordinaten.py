
# Aufgabe 4: Schachbrettkoordinaten

schachbrett = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", 
                "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", 
                "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", 
                "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", 
                "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", 
                "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", 
                "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
                "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"
               ]
"""
for i in range(0, 64, 8): # Schrittweite 8 damit jede Zeile neu begonnen wird (0-7, 8-15, 16-23, ...)
    print(schachbrett[i:i+8])

# Optimerung mit enumerate
for i, reihe in enumerate(range(0, 64, 8)):
    print(*schachbrett[reihe:reihe+8])
"""


x_k = "abcdefgh"
y_k = "12345678"

print("Tabelle der Kombinationen:\n")

for x in x_k:
    for y in y_k:
        print(f"{x}{y}", end="  ")  # z. B. a1, a2, a3 …
    print()  # Zeilenumbruch nach jeder Buchstabenreihe

    
