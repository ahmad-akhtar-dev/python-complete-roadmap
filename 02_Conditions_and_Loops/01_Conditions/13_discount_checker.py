"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

amount = float(input("Shopping amount: "))
if amount >= 5000:
    discount = amount * 0.10
elif amount >= 2000:
    discount = amount * 0.05
else:
    discount = 0
print("Discount =", discount)
print("Final bill =", amount - discount)
