"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import os
path = os.environ.get("PATH", "")
print(path.split(os.pathsep)[:5])
