"""
Remove Duplicates and Keep Order
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "19_remove_duplicates_keep_order.py"
"""

values = [3, 1, 3, 2, 1, 4]
unique = list(dict.fromkeys(values))
print(unique)

