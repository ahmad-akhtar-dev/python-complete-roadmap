"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

groups = {}
for name, section in [("Ali", "A"), ("Sara", "B"), ("Ahmad", "A")]:
    groups.setdefault(section, []).append(name)
print(groups)
