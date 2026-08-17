"""
Count Digits
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_count_digits.py"
"""

number = abs(int(input("Enter an integer: ")))
if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
        count += 1
        number //= 10
print("Digits:", count)

