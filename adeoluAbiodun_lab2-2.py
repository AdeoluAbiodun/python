# Name: Adeolu Abiodun  ||  Date: 08/16/2024  ||  Program file: adeoluAbiodun_lab2-2.py

# Program Description/Purpose: This program calculates the total amount of money in a savings account after a specific number of years based on the principal amount deposited, the annual interest rate, the number of times per year the interest is compounded, and the number of years the account will earn interest.

# Input/data entered from keyboard
prin = float(input("Enter the original amount deposited into the account: $"))
rate = float(input("Enter the annual interest rate (as a decimal, e.g. enter 0.05 for 5%): "))
nc = int(input("Enter the number of times per year the interest is compounded (e.g. 12 for monthly): "))
yrs = float(input("Enter the number of years the account will earn interest: "))

amt = prin*(1 + rate/nc)**(nc*yrs)

# Output both the original inputs and the calculated amount
print("\nOutputs")
print(f"Original deposit: ${prin:.2f}")
print(f"Annual interest rate: {rate:.2f}")
print(f"Number of times interest compounded per year: {nc}")
print(f"Time on deposit: {yrs:.2f} years")
print(f"Amount of money at the end of the period: ${amt:.2f}")