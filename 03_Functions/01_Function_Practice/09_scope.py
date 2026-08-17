"""
Local and Global Scope
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_scope.py"
"""

course = "Python"

def show_scope():
    topic = "Functions"
    print("Global variable inside function:", course)
    print("Local variable:", topic)

show_scope()
print("Global variable outside function:", course)

