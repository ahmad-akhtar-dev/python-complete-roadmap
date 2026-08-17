"""
Write CSV Data
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_write_csv.py"
"""

from pathlib import Path
import csv
file_path = Path(__file__).parent / "data" / "new_scores.csv"
rows = [["name", "score"], ["Ahmad", 90], ["Sara", 95]]
with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
print("CSV created:", file_path)

