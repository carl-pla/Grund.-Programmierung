class BankAccount: #Klassenmethode
    #Klassenattribute
    zinsen = 0.03 
    number_of_accounts = 0
    bank_name = "Rothschild"
    
    def __init__(self, inhaber, kontostand): 
        self._inhaber = inhaber 
        self._kontostand = kontostand
        BankAccount.number_of_accounts += 1
        
    
    def deposit(self, amount):
        """Guthaben aufladen"""
        if amount <= 0:
            raise ValueError("Beitrag muss positiv sein!")
        self._kontostand -= amount
        return self._kontostand
    
    def withdraw(self, amount): 
        """Guthaben abheben"""
        if amount <= 0:
            raise ValueError("Beitrag muss positiv sein!")
        if amount > self._kontostand: 
            raise ValueError("Nicht genügend Guthaben")
        self._kontostand += amount
        return self._kontostand
        
        
    def calculate_interest(self): 
        """Zinsen auf das Konto anwenden"""
        zinsen = self._kontostand * BankAccount.zinsen
        self._kontostand += zinsen
        return zinsen
    
    
    @staticmethod
    def is_amount_valid(amount): 
        """Einfache Validierung"""
        return amount > 0
     
    @classmethod
    def get_number_of_accounts(cls): 
        return cls.number_of_accounts
    
    @classmethod
    def set_bank_name(cls): 
        return cls.bank_name
    
#manuell testen 
konto1 = BankAccount("Tom", 3000)
konto1.deposit(100)
konto1.withdraw(300)
zinsen = konto1.calculate_interest()
bank_name = konto1.set_bank_name()

    
print(f"Inhaber: {konto1._inhaber}\nKontostand: {konto1._kontostand}\nZinsen: {zinsen}\nBankname: {bank_name}")
