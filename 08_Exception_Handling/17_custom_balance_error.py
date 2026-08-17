"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500
try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as error:
    print(error)
