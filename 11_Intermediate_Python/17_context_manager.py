"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
path = Path(__file__)
with path.open(encoding="utf-8") as file:
    first_line = file.readline().strip()
print(first_line)
