"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from datetime import date

def today_text():
    return date.today().isoformat()

print(today_text())
