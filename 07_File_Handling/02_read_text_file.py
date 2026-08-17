"""
Read a Text File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "02_read_text_file.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "notes.txt"
print(file_path.read_text(encoding="utf-8"))

