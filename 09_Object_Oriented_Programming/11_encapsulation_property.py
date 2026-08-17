"""
Encapsulation with Property
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "11_encapsulation_property.py"
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)

