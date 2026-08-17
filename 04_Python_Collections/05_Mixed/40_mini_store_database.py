"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

store = {1: {"name": "Mouse", "stock": 5}, 2: {"name": "Keyboard", "stock": 3}}
for product_id, product in store.items():
    print(product_id, product["name"], product["stock"])
