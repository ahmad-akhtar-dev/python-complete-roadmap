"""
Recursive Fibonacci
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_fibonacci.py"
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
print()

