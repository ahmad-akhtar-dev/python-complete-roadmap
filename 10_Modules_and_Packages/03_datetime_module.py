"""
Import datetime Module
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_datetime_module.py"
"""

from datetime import datetime
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M"))

