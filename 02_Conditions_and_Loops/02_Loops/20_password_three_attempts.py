"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

correct_password = "python"
attempt = 0
while attempt < 3:
    entered = input("Password: ")
    if entered == correct_password:
        print("Access granted")
        break
    attempt += 1
    print("Wrong password")
else:
    print("Account temporarily locked")
