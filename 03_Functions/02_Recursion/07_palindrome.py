"""
Recursive Palindrome Check
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_palindrome.py"
"""

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("python"))

