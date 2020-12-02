# Spencer, Tiffany, Michael (Shin), Nicky et al... :)
# Honorable mention: TA Christian for the challenge!

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = []
        self.accounts = {}

    def addAccount(self, accName):
        newAccount = BankAccount()
        self.accounts[accName] = newAccount

class BankAccount:
   
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate


    def deposit(self, amount):
        self.balance += amount
        print("Funds added to your account: +", amount)
        return self

Apollo = User("Apollo", "a@gmail.com")
Apollo.addAccount("Checking")
Apollo.addAccount("Savings")
Apollo.accounts["Checking"].deposit(50)

