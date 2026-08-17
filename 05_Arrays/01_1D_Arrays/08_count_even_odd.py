"""
1D Array: Count Even and Odd
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_count_even_odd.py"
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
even = sum(1 for n in numbers if n % 2 == 0)
odd = len(numbers) - even
print("Even:", even)
print("Odd:", odd)

