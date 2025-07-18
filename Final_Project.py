# Name: Adeolu Abiodun  ||  Date: 10/01/2020  ||  Program file: Adeolu_Abiodun_CSC121Project

# Program Description/Purpose: This Python program generates a cellular telephone bill, accepts cash payment, and instruct the cashier on how to provide the correct change

# Here are my Constants
BASE_COST = 15.00
RATES = {
    "under_60": 0.12,
    "50_to_120": 0.07,
    "over_120": 0.04
}

# Displaying my program main menu
def display_menu():
    print("Welcome to the CPCC Telephone System")
    print("1 — Create Single Telephone Bill")
    print("2 — Create Multiple Telephone Bills")
    print("3 — Quit")

# Calculating the amount owed/to be paid based on the number of minutes the customer used
def calc_amount_owed(minutes):
    if minutes < 60:
        return BASE_COST + (minutes * RATES["under_60"])
    elif 50 <= minutes <= 120:
        return BASE_COST + (minutes * RATES["50_to_120"])
    else:
        return BASE_COST + (minutes * RATES["over_120"])

# Ask for the amount received from the customer and validate it
def get_payment_amount(amount_owed):
    while True:
        try:
            payment = int(input("Enter the amount received from customer (in cents): "))
            if payment < 0:
                print("Please enter a valid amount.")
            elif payment < amount_owed * 100:  # Converting to cents
                print("The amount received is less than the amount owed.")
            else:
                return payment
        except ValueError:
            print("Invalid input. Please enter an integer value.")

# Calculate and display the change due to be given to the customer
def display_change(amount_owed, payment):
    change = payment - int(amount_owed * 100)  # Converting to cents
    dollars = change // 100
    quarters = (change % 100) // 25
    dimes = (change % 25) // 10
    nickels = (change % 10) // 5
    pennies = change % 5

    print("\nDenomination    Number")
    print(f"  Dollars        {dollars}")
    print(f"  Quarters       {quarters}")
    print(f"  Dimes          {dimes}")
    print(f"  Nickels        {nickels}")
    print(f"  Pennies        {pennies}")

# Validating that the state is a 2-letter code
def validate_state(state):
    return len(state) == 2 and state.isalpha()

# Validating that the zip code is a 5-digit number
def validate_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

# Here is to read customer data from the file and generate telephone bills
def process_data_file():
    try:
        with open('Downloads/TelephoneData.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):
                name = lines[i].strip()
                address = lines[i + 1].strip()
                city = lines[i + 2].strip()
                state = lines[i + 3].strip()
                zip_code = lines[i + 4].strip()
                minutes = int(lines[i + 5].strip())
                
                if not validate_state(state):
                    print(f"Invalid state for {name}. It should be a 2-letter code.")
                    continue
                if not validate_zip(zip_code):
                    print(f"Invalid zip code for {name}. It should be a 5-digit number.")
                    continue
                
                amount_owed = calc_amount_owed(minutes)
                
                # Display the bill
                print(f"\n{name}\n{address}\n{city}, {state} {zip_code}\n")
                print(f"Amount Owed: ${amount_owed:.2f}")

    except FileNotFoundError:
        print("Error: TelephoneData.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the telephone billing program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the customer: ")
            address = input("Enter street address: ")
            city = input("Enter city: ")
            state = input("Enter state (2-letter code): ")
            while not validate_state(state):
                state = input("Invalid state. Enter a valid 2-letter state code: ")
            zip_code = input("Enter zip code (5-digit number): ")
            while not validate_zip(zip_code):
                zip_code = input("Invalid zip code. Enter a valid 5-digit zip code: ")
            minutes = int(input("Enter the number of minutes used: "))

            amount_owed = calc_amount_owed(minutes)
            print(f"\n{name}\n{address}\n{city}, {state} {zip_code}\n")
            print(f"Amount Owed: ${amount_owed:.2f}")

            payment = get_payment_amount(amount_owed)
            display_change(amount_owed, payment)

        elif choice == '2':
            process_data_file()

        elif choice == '3':
            print("Thank you.")
            break

        else:
            print(f"{choice} is not a valid choice.")

if __name__ == "__main__":
    main()
