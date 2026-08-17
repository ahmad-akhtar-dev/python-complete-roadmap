"""
Recursive Countdown
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "01_countdown.py"
"""

def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)

