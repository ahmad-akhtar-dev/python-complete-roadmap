"""
Mini OOP Project: Library
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "19_library_project.py"
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title, "-", "Available" if book.available else "Borrowed")

library = Library()
library.add_book(Book("Python Basics"))
library.add_book(Book("OOP Made Easy"))
library.show_books()

