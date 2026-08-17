"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
folder = Path(__file__).parent / "data"
source = folder / "temporary_name.txt"
target = folder / "renamed_file.txt"
source.write_text("Rename practice", encoding="utf-8")
if target.exists():
    target.unlink()
source.rename(target)
print("Renamed to:", target.name)
