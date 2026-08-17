"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

package = input("Package name: ").strip()
print("Install command:", f"python -m pip install {package}" if package else "No package entered")
