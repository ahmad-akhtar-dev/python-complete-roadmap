"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import importlib.util
name = "requests"
print(name, "available?", importlib.util.find_spec(name) is not None)
