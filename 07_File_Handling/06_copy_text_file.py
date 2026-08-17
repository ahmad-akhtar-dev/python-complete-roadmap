"""
Copy a Text File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_copy_text_file.py"
"""

from pathlib import Path
base = Path(__file__).parent / "data"
source = base / "notes.txt"
destination = base / "notes_copy.txt"
destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
print("Copied to:", destination)

