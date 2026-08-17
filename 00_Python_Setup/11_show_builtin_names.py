"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import builtins
names = [name for name in dir(builtins) if not name.startswith("_")]
print("Some built-ins:", names[:20])
