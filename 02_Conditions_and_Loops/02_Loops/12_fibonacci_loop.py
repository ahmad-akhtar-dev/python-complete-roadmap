"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

terms = int(input("How many Fibonacci terms? "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()
