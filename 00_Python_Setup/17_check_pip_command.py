"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import shutil
pip_path = shutil.which("pip") or shutil.which("pip3")
print("pip found at:", pip_path if pip_path else "Not found")
