"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

cart = [{"name": "Mouse", "price": 1500, "qty": 2}, {"name": "Keyboard", "price": 3000, "qty": 1}]
total = sum(item["price"] * item["qty"] for item in cart)
print("Total:", total)
