"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from pathlib import Path
for item in Path.cwd().iterdir():
    print(item.name)
