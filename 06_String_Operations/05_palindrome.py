"""
Palindrome String
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_palindrome.py"
"""

text = input("Enter text: ").lower().replace(" ", "")
print("Palindrome" if text == text[::-1] else "Not a palindrome")

