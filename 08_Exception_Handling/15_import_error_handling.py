"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

try:
    import module_that_does_not_exist
except ImportError:
    print("Module could not be imported.")
