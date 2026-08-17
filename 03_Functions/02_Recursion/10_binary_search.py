"""
Recursive Binary Search
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_binary_search.py"
"""

def binary_search(values, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if values[middle] == target:
        return middle
    if target < values[middle]:
        return binary_search(values, target, low, middle - 1)
    return binary_search(values, target, middle + 1, high)

numbers = [2, 5, 8, 12, 16, 23, 38]
print("Index:", binary_search(numbers, 16, 0, len(numbers) - 1))

