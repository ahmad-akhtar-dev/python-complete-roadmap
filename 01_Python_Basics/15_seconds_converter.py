"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

seconds = int(input("Enter total seconds: "))
minutes, remaining_seconds = divmod(seconds, 60)
hours, remaining_minutes = divmod(minutes, 60)
print(f"{hours} hour(s), {remaining_minutes} minute(s), {remaining_seconds} second(s)")
