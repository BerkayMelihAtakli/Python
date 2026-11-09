class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(100)
account.withdraw(30)
print(account.balance)
account.withdraw(500)
print(account.balance)
account.deposit(-50)
print(account.balance)



# Een saldo onder nul en het storten van een negatief bedrag zouden niet mogen gebeuren.
# De methode zelf moet dit controleren (in plaats van de aanroepende code), omdat de klasse BankAccount zo altijd haar eigen data beschermt en voorkomt dat er vanaf een andere plek in het programma foutieve gegevens worden ingevoerd.