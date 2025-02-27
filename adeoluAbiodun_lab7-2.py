# Name: Adeolu Abiodun  ||  Date: 09/25/2024  ||  Program file: adeoluAbiodun_lab7-2.py

# Program Description/Purpose: This program uses a loop to step through a list and display a two-dimensional list with all of the integers being either prime or composite.

def is_prime(number):
    # Returns True if the number is prime, otherwise False
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def populate_number_list(n):
    number_list = [[i] for i in range(2, n + 1)]
    return number_list

def classify_numbers(number_list):
    # Classifies each number in the list as prime or composite
    for sublist in number_list:
        number = sublist[0]
        if is_prime(number):
            sublist.append('prime')
        else:
            sublist.append('composite')
    return number_list

def display_results(number_list):
    # Displays each number with its classification
    for sublist in number_list:
        print(f"{sublist[0]} is {sublist[1]}")

def get_user_input():
    # Requesting user input and offering feedback if the input is invalid
    while True:
        try:
            n = int(input("Enter an integer greater than 24: "))
            if n <= 24:
                print("Inputted/entered number cannot be less than 25.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Main function
    n = get_user_input()

    number_list = populate_number_list(n)
    classified_numbers = classify_numbers(number_list)

    # Display the results
    display_results(classified_numbers)

# Start the program
if __name__ == '__main__':
    main()