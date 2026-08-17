"""
Factorial with While Loop
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_factorial_while.py"
"""

n = int(input("Enter a non-negative integer: "))
factorial = 1
current = 1
while current <= n:
    factorial *= current
    current += 1
print("Factorial:", factorial)

