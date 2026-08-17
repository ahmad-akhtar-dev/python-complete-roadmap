"""
Variable Keyword Arguments
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_kwargs.py"
"""

def show_profile(**profile):
    for key, value in profile.items():
        print(f"{key}: {value}")

show_profile(name="Ahmad", city="Lahore", skill="Python")

