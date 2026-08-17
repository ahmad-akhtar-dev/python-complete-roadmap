"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

scores = {"Sara": 91, "Ali": 80, "Ahmad": 88}
for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
    print(name, score)
