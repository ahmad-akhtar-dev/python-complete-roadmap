"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def launch_countdown(number):
    if number == 0:
        print("Go!")
        return
    print(number)
    launch_countdown(number - 1)

launch_countdown(5)
