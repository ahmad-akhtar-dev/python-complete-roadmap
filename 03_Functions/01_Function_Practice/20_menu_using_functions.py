"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

choice = input("Choose + or -: ")
a = float(input("First number: "))
b = float(input("Second number: "))
if choice == "+":
    print(add(a, b))
elif choice == "-":
    print(subtract(a, b))
else:
    print("Invalid choice")
