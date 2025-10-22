x = [2, 4, 7]
y = [3, 4, 2]

tupel_summe = ()
for k in range(len(x)): 
    summe_komponenten = x[k] + y[k]
    tupel_summe = tupel_summe + (summe_komponenten)
    
print(tupel_summe)
