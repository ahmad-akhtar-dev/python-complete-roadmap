"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def is_valid_username(username):
    return len(username) >= 4 and username.replace("_", "").isalnum()

print(is_valid_username("ahmad_dev"))
