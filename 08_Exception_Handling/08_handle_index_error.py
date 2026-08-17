"""
Handle IndexError
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_handle_index_error.py"
"""

colors = ["red", "green", "blue"]
try:
    print(colors[5])
except IndexError:
    print("That list position does not exist.")

