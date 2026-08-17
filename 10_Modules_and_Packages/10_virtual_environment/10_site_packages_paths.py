"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import site
print("Site-packages locations:")
for path in site.getsitepackages():
    print(path)
