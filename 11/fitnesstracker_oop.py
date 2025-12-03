class Fitnesstracker: 
    #Klassenattribute
    anzahl_accounts = 0
    trainer = ""
    #account_id = 0
    #steps = 0 ==> kann direkt als Instanzattribut der __init__-Methode mitgegeben werden, außerdem gilt nicht global für alle
    
    def __init__(self, user, steps=0, workout=None, calories_burned=0): 
        self.__user = user 
        self.__steps = steps
        self.__workout = workout if workout else []
        self.__calories_burned = calories_burned
        Fitnesstracker.anzahl_accounts += 1
    
    #Getter Methoden
    
    def get_user(self):
        return self.__user
    
    def get_steps(self):
        return self.__steps
    
    def get_calories(self):
        return self.__calories
    
    def get_workout(self): 
        return self.__workout
    
       
    #Methoden zur Veränderung von Instanzdaten 
    
    def add_steps(self, steps):
        if self.is_input_valid(steps):
            self.__steps += steps
    
      
    def burn_calories(self, calories):
        if self.is_input_valid(calories):
            self.__calories_burned += calories
        
    def log_workout(self, workout):
        self.__workout.append(workout)
        
    #Zusammenfassung    

    def summary(self): 
        return f"User: {self.__user}\nsteps: {self.__steps}\nworkout: {self.__workout}\nburned calories: {self.__calories_burned} "
    
    #statische Methoden für Validierung
        
    @staticmethod
    def is_input_valid(value): 
        if value < 0: 
            raise ValueError("Der Wert muss positiv sein")
        return True    
    
    @classmethod   
    def get_anzahl_accounts(cls):
        return cls.anzahl_accounts
    
    @classmethod 
    def get_trainer(cls, name):
        cls.trainer = name
        
    

#manuelle Tesdaten        
benutzer1 = Fitnesstracker("Max")
benutzer1.add_steps(1000)
benutzer1.burn_calories(200)
benutzer1.log_workout("HIIT")
print(benutzer1.summary())

#Klassenattribute testen
Fitnesstracker.get_trainer("Coach Ben")
print("Trainer", Fitnesstracker.trainer)
print("Anzahl Accounts:", Fitnesstracker.get_anzahl_accounts())