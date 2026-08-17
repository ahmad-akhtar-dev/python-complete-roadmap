"""
The __str__ Method
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "17_dunder_str.py"
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

print(Book("Learn Python", "Ahmad"))

