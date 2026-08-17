"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

character = input("Enter one character: ")
if len(character) != 1:
    print("Please enter exactly one character.")
elif character.isalpha():
    print("Alphabet")
elif character.isdigit():
    print("Digit")
else:
    print("Special character")
