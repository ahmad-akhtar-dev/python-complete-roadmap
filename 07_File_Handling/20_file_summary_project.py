"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
path = Path(__file__).parent / "data" / "notes.txt"
text = path.read_text(encoding="utf-8")
print("Characters:", len(text))
print("Words:", len(text.split()))
print("Lines:", len(text.splitlines()))
