"""
Sum from 1 to N
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_sum_1_to_n.py"
"""

n = int(input("Enter N: "))
total = 0
for number in range(1, n + 1):
    total += number
print("Sum:", total)

