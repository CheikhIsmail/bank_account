from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        self.account_type = "Generic"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.now(), "Deposit", amount, self.balance))
            print(f"Deposited {amount} units. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.now(), "Withdraw", amount, self.balance))
            print(f"Withdrew {amount} units. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
    
    def display_transactions(self):
        print(f"Transaction History for Account Number: {self.account_number}")
        for date, trans_type, amount, balance in self.transactions:
            print(f"{date} - {trans_type}: {amount} units, Balance: {balance}")

    def calculate_interest(self, rate, months):
        if self.account_type == "Savings":
            interest = self.balance * (rate / 100) * (months / 12)
            self.balance += interest
            self.transactions.append((datetime.now(), "Interest", interest, self.balance))
            print(f"Calculated interest: {interest} units. New balance: {self.balance}")
        else:
            print("Interest calculation is only available for savings accounts.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.account_type = "Savings"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.account_type = "Checking"
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append((datetime.now(), "Withdraw", amount, self.balance))
            print(f"Withdrew {amount} units. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount, including overdraft limit.")


def main():
    # Create a savings account and a checking account
    savings_account = SavingsAccount(account_number="871411")
    checking_account = CheckingAccount(account_number="871412", overdraft_limit=500)
    
    # Deposit money into the savings account
    savings_account.deposit(10000)
    
    # Withdraw money from the savings account
    savings_account.withdraw(500)
    
    # Display balance of the savings account
    savings_account.display_balance()
    
    # Display transactions of the savings account
    savings_account.display_transactions()
    
    # Calculate and add interest to the savings account
    savings_account.calculate_interest(rate=5, months=12)
    
    # Display balance after interest
    savings_account.display_balance()
    
    # Deposit money into the checking account
    checking_account.deposit(2000)
    
    # Withdraw money from the checking account, testing overdraft
    checking_account.withdraw(2500)
    
    # Display balance of the checking account
    checking_account.display_balance()
    
    # Display transactions of the checking account
    checking_account.display_transactions()

if __name__ == "__main__":
    main()
