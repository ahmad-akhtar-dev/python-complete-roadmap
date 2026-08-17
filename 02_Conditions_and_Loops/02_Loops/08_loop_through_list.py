"""
Loop Through a List
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_loop_through_list.py"
"""

subjects = ["Python", "Java", "Web", "Database"]
for index, subject in enumerate(subjects, start=1):
    print(index, subject)

