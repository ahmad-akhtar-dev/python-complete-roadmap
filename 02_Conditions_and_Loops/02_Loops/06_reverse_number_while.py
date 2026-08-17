"""
Reverse a Number with While Loop
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_reverse_number_while.py"
"""

number = int(input("Enter a positive integer: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("Reversed:", reversed_number)

