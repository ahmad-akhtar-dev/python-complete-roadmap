"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import csv
from pathlib import Path
path = Path(__file__).parent / "data" / "students_dict.csv"
rows = [{"name": "Ali", "marks": 80}, {"name": "Sara", "marks": 92}]
with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(rows)
print("CSV saved.")
