"""
Append to a Text File
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_append_text_file.py"
"""

from pathlib import Path
file_path = Path(__file__).parent / "data" / "my_note.txt"
with file_path.open("a", encoding="utf-8") as file:
    file.write("I also learned append mode.\n")
print("New line appended.")

