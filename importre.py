import re

# Constants for base cost and per minute fees
BASE_COST = 15.00
FEE_UNDER_60 = 0.12
FEE_60_TO_120 = 0.07
FEE_OVER_120 = 0.04

# File name for data file processing
DATA_FILE = 'Downloads/TelephoneData.txt'

# Displays the main menu options
def displayMenu():
    print("\nWelcome to the CPCC Telephone System")
    print("1 - Create Single Telephone Bill")
    print("2 - Create Multiple Telephone Bills (No Payment Processing)")
    print("3 - Quit")

# Calculates the amount owed based on the number of minutes spent/used
def calcAmountOwed(minutes):
    if minutes < 60:
        return BASE_COST + (minutes * FEE_UNDER_60)
    elif 60 <= minutes <= 120:
        return BASE_COST + (minutes * FEE_60_TO_120)
    else:
        return BASE_COST + (minutes * FEE_OVER_120)

# Formats and validates the customer input
def formatCustomerInfo(prompt):    
    while True:
        value = input(prompt).strip()
        if value:
            return value.title()
        else:
            print("This field cannot be empty. Please enter a valid value.")

# Prompts user for customer input and returns it as a tuple
def getCustomerInfo():
    name = formatCustomerInfo("Enter the name of the customer: ")
    address = formatCustomerInfo("Enter street address: ")
    city = formatCustomerInfo("Enter city: ")
    state = input("Enter state (2-letter abbreviation): ").strip().upper()
    while not re.match(r"^[A-Z]{2}$", state):
        print("Invalid state format. Please enter a valid 2-letter state abbreviation.")
        state = input("Enter state (2-letter abbreviation): ").strip().upper()
    zip_code = input("Enter zip code: ").strip()
    while not re.match(r"^\d{5}(-\d{4})?$", zip_code):
        print("Invalid zip code format. Please enter a valid 5 or 9-digit zip code.")
        zip_code = input("Enter zip code: ").strip()
    return name, address, city, state, zip_code

# Prompts the user for the number of minutes used and validates it
def getMinutesUsed():
    while True:
        try:
            minutes = int(input("Enter the number of minutes used: "))
            if minutes < 0:
                print("Minutes used cannot be negative. Please enter a positive value.")
            else:
                return minutes
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Creates a single telephone bill for the user
def createSingleTelephoneBill():
    name, address, city, state, zip_code = getCustomerInfo()
    minutes = getMinutesUsed()
    amount_owed = calcAmountOwed(minutes)
    
# Display the bill information
    print(f"\n{name}")
    print(f"{address}")
    print(f"{city}, {state}  {zip_code}")
    print(f"\nAmount Owed: ${amount_owed:.2f}")

# Reads customer data from a file and processes multiple records
def processMultipleBills():
    try:
        with open(DATA_FILE, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6:
                    name, address, city, state, zip_code, minutes = data[0], data[1], data[2], data[3], data[4], data[5]
                    try:
                        minutes = int(minutes)
                    except ValueError:
                        print(f"Skipping record due to invalid minutes value: {line}")
                        continue

                    amount_owed = calcAmountOwed(minutes)
                    
    # Display each customer's bill
                    print(f"\n{name}")
                    print(f"{address}")
                    print(f"{city}, {state}  {zip_code}")
                    print(f"Amount Owed: ${amount_owed:.2f}")
                else:
                    print(f"Skipping invalid record: {line}")
    except FileNotFoundError:
        print(f"Error: {DATA_FILE} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the program
def main():
    while True:
        displayMenu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                createSingleTelephoneBill()
            elif choice == 2:
                processMultipleBills()
            elif choice == 3:
                print("Thank you.")
                break
            else:
                print(f"{choice} is not a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

# Start the program
if __name__ == '__main__':
    main()