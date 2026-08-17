"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import math
public_names = [name for name in dir(math) if not name.startswith("_")]
print(public_names[:15])
