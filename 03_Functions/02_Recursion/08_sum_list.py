"""
Recursive List Sum
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_sum_list.py"
"""

def list_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + list_sum(numbers[1:])

print(list_sum([10, 20, 30, 40]))

