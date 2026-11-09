class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True


account = BankAccount(100)
print(account.withdraw(30), account.balance)
print(account.withdraw(500), account.balance)
print(account.withdraw(-5), account.balance)
print(account.deposit(0), account.balance)
print(account.deposit(25), account.balance)

# Als een methode False teruggeeft, stopt de methode direct door het 'return False' statement.