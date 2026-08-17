"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

tasks = []
tasks.append("Learn lists")
tasks.append("Practice Python")
print("Task list:")
for index, task in enumerate(tasks, start=1):
    print(index, task)
