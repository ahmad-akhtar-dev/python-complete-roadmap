"""
Dictionary Add, Update, Remove
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "14_add_update_remove.py"
"""

profile = {"name": "Ahmad", "city": "Lahore"}
profile["skill"] = "Python"
profile["city"] = "Islamabad"
profile.pop("skill")
print(profile)

