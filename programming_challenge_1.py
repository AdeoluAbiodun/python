# Name: Adeolu Abiodun  ||  Date: 01/23/2025  ||  Program file: programming_challenge_1.py

# This modular Python program prompts user for input, calculates a value using the formula (Q = Square root of [(2 * C * D)/H]), and then displays the result

import math

def calculate_Q(D_values):
    # Calculates the Q values using the formula: Q = Square root of [(2 * C * D) / H]
    # Constants: C = 50 and H = 30
    C = 50
    H = 30
    result = []
    for D in D_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(round(Q))
    return result

def parse_input(input_string): # Takes a string of comma-separated numbers and converts it into a list of floats.
    
    try:
       return [float(value) for value in input_string.split(",")]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return []

# Below is the main function that controls the program. It asks the user for input, calculates Q values, and displays the results.
# The program will keep running until the user decides to stop.
def main():
    while True:
        input_string = input("Enter your numbers separated by a comma: ")


        items = parse_input(input_string)

        if items:
            value = calculate_Q(items)

            print("The calculated values are: ", ", ".join(map(str, value)))

        
        choice = input("Would you like to run the program again? Enter 1 for yes or any other key to exit: ") # Ask user if they want to run the program again.
        if choice.strip() != "1":
            print("Thank you and Goodbye!")
            break

if __name__ == "__main__":
    main()

