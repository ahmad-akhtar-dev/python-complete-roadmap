"""
Simple Menu with Conditions
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_simple_menu.py"
"""

print("1. View profile")
print("2. View courses")
print("3. Exit")
choice = input("Choose 1, 2, or 3: ")

if choice == "1":
    print("Profile opened.")
elif choice == "2":
    print("Courses opened.")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice.")

