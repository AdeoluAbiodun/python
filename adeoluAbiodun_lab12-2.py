# Name: Adeolu Abiodun  ||  Date: 03/22/2025  ||  Program file: adeoluAbiodun_lab12-2.py

# This Python program creates the function ackermann(m, n) and tests it with a few example inputs.


import sys

Recursion_Limit = 1000
sys.setrecursionlimit(Recursion_Limit)

# Here is the Ackermann function with m and n
def ackermann(m, n):
    
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

def check_ackermann(m, n):

    if m < 0 or n < 0:
        return "Negative numbers are not accepted. Please enter positive values."
    
    if m > 3 or (m == 3 and n > 6):
        return "Warning: Values too large and exceed the recursion limit!"
    
    try:
        result = ackermann(m, n)
        return f"Ackermann({m}, {n}) = {result}"
    except RecursionError:
        return "Error: Values too large"

# Testing the function with a few inputs
print(check_ackermann(0, 0))
print(check_ackermann(0, 1))
print(check_ackermann(1, 2))
print(check_ackermann(2, 4))
print(check_ackermann(3, 6))
print("=====================")
print(check_ackermann(4, 8))
print("=========================================================")
print(check_ackermann(-1, -2))
