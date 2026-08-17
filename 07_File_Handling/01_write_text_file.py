"""
Write a Text File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "01_write_text_file.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "my_note.txt"
file_path.write_text("Today I practiced Python file handling.\n", encoding="utf-8")
print("Written to:", file_path)

