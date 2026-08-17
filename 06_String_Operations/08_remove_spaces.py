"""
Remove Extra Spaces
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_remove_spaces.py"
"""

text = "Python   is   easy   to learn"
clean = " ".join(text.split())
print(clean)

