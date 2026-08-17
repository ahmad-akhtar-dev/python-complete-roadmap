"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))
bmi = weight / (height ** 2)
print("BMI =", round(bmi, 2))
