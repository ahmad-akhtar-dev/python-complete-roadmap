"""
Leap Year Check
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_leap_year.py"
"""

year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

