"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

text = "PyThOn"
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print("Upper:", upper, "Lower:", lower)
