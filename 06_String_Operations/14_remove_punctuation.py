"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import string
text = "Hello, Python! How are you?"
clean = "".join(c for c in text if c not in string.punctuation)
print(clean)
