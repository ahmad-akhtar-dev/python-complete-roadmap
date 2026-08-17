"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def get_grade(marks):
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 50:
        return "D"
    return "F"

print("Grade:", get_grade(76))
