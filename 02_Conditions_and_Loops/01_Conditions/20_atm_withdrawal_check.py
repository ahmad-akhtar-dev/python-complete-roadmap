"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

balance = 10000
amount = float(input("Amount to withdraw: "))
if amount <= 0:
    print("Enter a positive amount.")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Withdrawal successful. Remaining balance =", balance)
