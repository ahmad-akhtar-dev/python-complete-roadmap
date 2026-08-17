"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

principal = float(input("Principal amount: "))
rate = float(input("Rate: "))
time = float(input("Time in years: "))
interest = principal * rate * time / 100
print("Simple interest =", interest)
