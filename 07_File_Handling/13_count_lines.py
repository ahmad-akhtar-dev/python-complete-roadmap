"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
path = Path(__file__).parent / "data" / "notes.txt"
with path.open(encoding="utf-8") as file:
    print("Lines:", sum(1 for _ in file))
