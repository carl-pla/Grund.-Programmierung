# Aufgabe 1: Bioninalkoeffizient 
# a)
def fakultaet(n): 
    if n == 0 or n == 1: 
        return 1 
    else: 
        output = n * fakultaet(n-1)
        return output
    
    
#fakultaet(5)
n = int(input("Geben Sie eine Zahl n ein: "))
print(f"Die Fakultät von {n} ist {fakultaet(n)}")    

# b)
def binominal(n, k):
    if k > n:
        return 0
    else:
        return fakultaet(n) // (fakultaet(k) * fakultaet(n - k))
    
print(f"Der Bionominalkoeffizient ist: {binominal(6, 2)}")