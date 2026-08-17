"""
Recursive GCD
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_gcd.py"
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))

