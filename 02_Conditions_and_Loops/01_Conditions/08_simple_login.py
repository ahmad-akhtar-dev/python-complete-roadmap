"""
Simple Login Check
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_simple_login.py"
"""

correct_username = "admin"
correct_password = "python123"

username = input("Username: ")
password = input("Password: ")
if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")

