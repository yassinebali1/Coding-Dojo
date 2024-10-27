class BankAccount:  
    accounts = []

    def __init__(self, int_rate=0.01, balance=0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5  
            print(f"New balance after fee: ${self.balance}.")

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}, Interest Rate: {self.int_rate:.2%}")

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Interest yielded: ${interest:.2f}. New balance: ${self.balance:.2f}.")

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            account.display_account_info()


account1 = BankAccount(int_rate=0.01, balance=100)
account2 = BankAccount(int_rate=0.02, balance=200)

account1.deposit(50).deposit(25).withdraw(30).yield_interest().display_account_info()
account2.deposit(100).withdraw(50).withdraw(30).withdraw(20).withdraw(10).yield_interest().display_account_info()
BankAccount.print_all_accounts_info()
