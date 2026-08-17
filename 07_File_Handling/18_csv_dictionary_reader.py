"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import csv
from pathlib import Path
path = Path(__file__).parent / "data" / "scores.csv"
with path.open(encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row)
