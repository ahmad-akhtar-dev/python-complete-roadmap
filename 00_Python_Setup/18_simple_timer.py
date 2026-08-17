"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

from time import perf_counter
start = perf_counter()
result = sum(range(1000))
end = perf_counter()
print("Result:", result)
print("Time used:", round(end - start, 6), "seconds")
