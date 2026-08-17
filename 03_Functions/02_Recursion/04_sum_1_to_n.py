"""
Recursive Sum 1 to N
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_sum_1_to_n.py"
"""

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(10))

