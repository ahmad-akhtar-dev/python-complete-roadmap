"""
Largest of Three Numbers
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_largest_of_three.py"
"""

a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

