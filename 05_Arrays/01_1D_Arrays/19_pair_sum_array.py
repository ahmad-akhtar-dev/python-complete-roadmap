"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

values = [2, 7, 11, 15]
target = 9
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] + values[j] == target:
            print("Pair:", values[i], values[j])
