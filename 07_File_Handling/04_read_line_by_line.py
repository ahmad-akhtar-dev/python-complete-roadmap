"""
Read File Line by Line
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_read_line_by_line.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "names.txt"
with file_path.open("r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

