#b)

zeilen = []
sammelwert = 0

with open("zahlen.txt", "r") as z:
    for line in z: 
        zahl = int(line.rstrip())
        sammelwert += zahl / 30
    
    print(sammelwert)
    z.close()

with open("sw.csv", "r") as z:
    for line in z: 
        print(line)