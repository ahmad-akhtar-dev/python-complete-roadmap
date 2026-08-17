"""
Read CSV Data
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_read_csv.py"
"""

from pathlib import Path
import csv
file_path = Path(__file__).parent / "data" / "scores.csv"
with file_path.open("r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["score"])

