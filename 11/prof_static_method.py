class BankAccount:
    number_of_accounts = 0
    bank_name = ""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        #Wichtig: Für Klassenattribute, die in __init__ verändert werden, nicht self verwenden.
        # Ansonsten wird zusätzlich ein Instanzattribut erzeugt (mit demselben Namen!)
        BankAccount.number_of_accounts += 1

    @staticmethod
    def is_amount_valid(amount):
        if amount >= 0:
            return True
        else:
            return False

    def deposit(self, amount):
        if self.is_amount_valid(amount):
            self.balance += amount

    def withdraw(self, amount):
        if self.is_amount_valid(amount) and self.balance >= amount:
            self.balance -= amount

    @classmethod
    def get_number_of_accounts(cls):
        return cls.number_of_accounts

    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def calculate_interest(amount, rate):
        """
        :param amount: amount to calculate interest for
        :param rate: interest rate in percent
        :return: interest
        """
        return amount * (rate / 100)


bank_account_luke = BankAccount("Luke", 1000)
bank_account_yoda = BankAccount("Yoda", 500)
bank_account_jabba = BankAccount("Jabba", 10000)
BankAccount.set_bank_name("Sparkasse")

bank_account_jabba.withdraw(100)

print(f"Anzahl Konten: {BankAccount.number_of_accounts}")
print(f"Bankname: {BankAccount.bank_name}")
print(f"Kontostand von {bank_account_jabba.owner}: {bank_account_jabba.balance}")
