"""
Mini OOP Project: Bank Account
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "18_bank_account_project.py"
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

account = BankAccount("Ahmad", 1000)
account.deposit(500)
account.withdraw(300)
print(account.owner, account.balance)

