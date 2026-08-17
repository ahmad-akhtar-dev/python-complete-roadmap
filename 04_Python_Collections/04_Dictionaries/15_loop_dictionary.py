"""
Loop Through Dictionary
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "15_loop_dictionary.py"
"""

marks = {"Python": 90, "Java": 82, "Web": 88}
for subject, score in marks.items():
    print(subject, "->", score)

