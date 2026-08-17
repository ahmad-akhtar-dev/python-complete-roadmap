"""
Break Statement: Search
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_break_search.py"
"""

numbers = [4, 8, 15, 16, 23, 42]
target = int(input("Number to search: "))
for number in numbers:
    if number == target:
        print("Found:", target)
        break
else:
    print("Not found")

