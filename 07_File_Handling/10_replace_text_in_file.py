"""
Replace Text in a File Copy
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_replace_text_in_file.py"
"""

from pathlib import Path
base = Path(__file__).parent / "data"
source = base / "notes.txt"
destination = base / "notes_updated.txt"
text = source.read_text(encoding="utf-8")
updated = text.replace("simple", "friendly")
destination.write_text(updated, encoding="utf-8")
print("Updated copy saved:", destination)

