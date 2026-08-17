"""
Split an Email Address
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_email_parts.py"
"""

email = "ahmad@example.com"
username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)

