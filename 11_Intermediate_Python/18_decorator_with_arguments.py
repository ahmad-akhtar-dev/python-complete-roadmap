"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello", name)

greet("Ahmad")
