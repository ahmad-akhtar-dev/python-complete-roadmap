"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

secret = 7
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3 - Guess: "))
    if guess == secret:
        print("Correct!")
        break
else:
    print("No attempts left. The number was", secret)
