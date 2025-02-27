# Name: Adeolu Abiodun  ||  Date: 08/28/2024  || Program File: adeoluAbiodun_lab3-2.py
# Program Description/Purpose: This is a money counting game. The program requires input of pennies, nickels, dimes, and quarters and calculates the total of the coins to determine if the user wins or not.

# Ask user for inputs
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

# Calculate the total value of the coins entered and display the value/total
total_value = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

print(f"\nTotal value of coins entered: ${total_value:.2f}")

# Final Result(s)
if total_value == 1.00:
    print("Congratulations! The value of the coins you entered is $1.00!")
elif total_value < 1.00:
    difference = 1.00 - total_value
    print(f"The difference between the value you entered and the expected value of $1.00 is ${difference:.2f}.")
else:
    difference = total_value - 1.00
    print(f"The difference between the value you entered and the expected value of $1.00 is ${difference:.2f}.")