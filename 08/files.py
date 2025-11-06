#b)

zeilen = []
sammelwert = 0

with open("zahlen.txt", "r") as z:
    for line in z: 
        zahl = int(line.rstrip())
        sammelwert += zahl / 500
    
    print(sammelwert)
    z.close()

"""with open("sw.csv", "r") as z:
    z.reader = csv.reader(z)
    for line in z: 
        print(line)"""