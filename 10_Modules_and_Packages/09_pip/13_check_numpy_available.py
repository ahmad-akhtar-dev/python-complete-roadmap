"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import importlib.util
name = "numpy"
print(name, "available?", importlib.util.find_spec(name) is not None)
