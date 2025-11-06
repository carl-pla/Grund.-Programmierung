import random as rd 

#a)

a = 0
b = 100 

def random(): 
    with open ("zahlen.txt", "a") as z:
        
        for _ in range(500): 
            zufall = rd.randint(a,b)
            print(zufall)
            z.write(str(zufall) + "\n")
           
random()


   



        