"""
Search Text in a File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_search_text_in_file.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "notes.txt"
keyword = "GitHub"
for line_number, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
    if keyword.lower() in line.lower():
        print(f"Found on line {line_number}: {line}")

