"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
path = Path(__file__).parent / "data" / "study_plan.txt"
lines = ["Python basics\n", "Functions\n", "OOP\n"]
with path.open("w", encoding="utf-8") as file:
    file.writelines(lines)
print("Study plan saved.")
