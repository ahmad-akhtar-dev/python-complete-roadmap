"""
Decorators
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_decorators.py"
"""

def announce(function):
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = function(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper

@announce
def greet(name):
    print(f"Hello, {name}!")

greet("Ahmad")

