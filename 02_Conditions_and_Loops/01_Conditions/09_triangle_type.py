"""
Triangle Type
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_triangle_type.py"
"""

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle.")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

