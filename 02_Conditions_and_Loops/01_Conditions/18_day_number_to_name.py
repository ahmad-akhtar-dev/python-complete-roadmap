"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

day = int(input("Enter day number (1-7): "))
names = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
print(names.get(day, "Invalid day number"))
