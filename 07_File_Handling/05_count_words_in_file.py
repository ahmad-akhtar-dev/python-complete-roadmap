"""
Count Words in a File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_count_words_in_file.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "notes.txt"
text = file_path.read_text(encoding="utf-8")
print("Word count:", len(text.split()))

