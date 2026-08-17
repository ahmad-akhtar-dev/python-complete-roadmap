"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
path = Path(__file__).parent / "data" / "notes.txt"
print(path.read_text(encoding="utf-8"))
