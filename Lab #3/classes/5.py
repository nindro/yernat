class Account:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Amount of withdraw must be positive")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
acct = Account("John Doe", 100)
print(acct)
acct.deposit(50)
acct.withdraw(30)
acct.withdraw(200)
acct.deposit(-10)

print(acct)