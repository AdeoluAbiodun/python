
# Name: Adeolu Abiodun  ||  Date: 10/02/2020  ||  Program file: Adeolu_Abiodun_CSC121FinalExam_Skates

# Program Description/Purpose: This program is to calculate the cost of purchasing skates

# Here are the constants for skate prices and tax rate
Price_of_Roller_Skates_1_4 = 154.75
Price_of_Roller_Skates_5_Plus = 137.50
Price_of_Roller_Blades_1_4 = 229.95
Price_of_Roller_Blades_5_Plus = 188.95
Sales_Tax_Rate = 0.0675

# Below is the function that displays the skate selection menu
def display_menu():
    print("1. Roller Skates")
    print("2. Roller Blades")
    print()

# Below is the function that get the user's skate choice and validate input
def get_skate_choice():
    while True:
        try:
            choice = int(input("Please select the type of skates you'd like to purchase (1 for Roller Skates, 2 for Roller Blades): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

# Here is the function that get the number of pairs and validate input
def get_number_of_pairs():
    while True:
        try:
            number_of_pairs = int(input("How many pairs of skates would you like to purchase? "))
            if number_of_pairs >= 1:
                return number_of_pairs
            else:
                print("You must buy at least 1 pair of skates.")
        except ValueError:
            print("Invalid input. Please enter a valid number of pairs.")

# Below is the function that calculate the subtotal based on skate type and number of pairs
def calculate_subtotal(choice, number_of_pairs):
    if choice == 1:  # Roller Skates
        if number_of_pairs <= 4:
            return number_of_pairs * Price_of_Roller_Skates_1_4
        else:
            return number_of_pairs * Price_of_Roller_Skates_5_Plus
    elif choice == 2:  # Roller Blades
        if number_of_pairs <= 4:
            return number_of_pairs * Price_of_Roller_Blades_1_4
        else:
            return number_of_pairs * Price_of_Roller_Blades_5_Plus

# Below is the function that calculate sales tax
def calculate_tax(subtotal):
    return subtotal * Sales_Tax_Rate

# Below is the function that display the results with proper formatting
def display_results(choice, number_of_pairs, subtotal, tax, total):
    skate_type = "Roller Skates" if choice == 1 else "Roller Blades"
    print(f"\nThe customer purchased {number_of_pairs} pair(s) of {skate_type}.")
    print(f"The cost is           ${subtotal:,.2f}")
    print(f"The sales tax is      ${tax:,.2f}")
    print(f"The total charge is   ${total:,.2f}")

# My Main function
def main():
    display_menu()
    choice = get_skate_choice()
    number_of_pairs = get_number_of_pairs()
    subtotal = calculate_subtotal(choice, number_of_pairs)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    display_results(choice, number_of_pairs, subtotal, tax, total)

# Run the program
if __name__ == "__main__":
    main()
