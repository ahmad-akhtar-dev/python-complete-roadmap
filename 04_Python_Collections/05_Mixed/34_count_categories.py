"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

items = [("Laptop", "Tech"), ("Mouse", "Tech"), ("Book", "Study")]
counts = {}
for _, category in items:
    counts[category] = counts.get(category, 0) + 1
print(counts)
