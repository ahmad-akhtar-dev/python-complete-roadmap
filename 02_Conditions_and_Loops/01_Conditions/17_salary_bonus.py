"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

salary = float(input("Monthly salary: "))
years = int(input("Years of service: "))
bonus = salary * 0.10 if years >= 5 else salary * 0.05
print("Bonus =", bonus)
