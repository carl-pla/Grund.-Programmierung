import random as rd 

#a)

a = 0
b = 100 

def random(): 
    for _ in range(0,10): 
        zufall = rd.randint(a,b)
        print(f"{zufall}")

print(random())



        