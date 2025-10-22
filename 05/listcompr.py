import math

# Aufgabe 1 a) 

def teilbar(): 
    n = int(input("Geben Sie ein Zahl ein: "))
    while 0 <= n: 
        if n %2 == 0 and n %3 == 0: 
            print(n)
            n -=1
        else: 
            n -= 1
        if n <= 0: 
            print("Zahl ist kleiner 0")
            break

            
teilbar()

# b) 

def quadrat():
    n = int(input("Geben Sie eine Zahl ein: "))

    while n >= 0:
        if n % 3 == 0:
            wurzel = int(n ** 0.5)  
            if wurzel * wurzel == n:
                print(n)
        n -= 1

    print("Fertig — alle Zahlen geprüft.")

quadrat()