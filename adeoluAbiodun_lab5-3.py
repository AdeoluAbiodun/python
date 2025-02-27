# Name: Adeolu Abiodun  ||  Date: 09/04/2024  ||  Program file: adeoluAbiodun_lab5-3.py

# Program Description/Purpose: This is a modular Python program created to estimate the total cost of a paint job for Freddie Sam Bob's OK Paint company.

# Here is the main function
def main():
    while True:
        num_rooms, total_square_feet = numRooms()
        price_per_gallon = paintPrice()
        gallons_required, hours_required, paint_cost, labor_cost, total_cost = calcCost(total_square_feet, price_per_gallon)
        printResults(total_square_feet, gallons_required, hours_required, paint_cost, labor_cost, total_cost)
        
        # Asking the user if they want another estimate
        another = input('Another estimate? (y=yes, enter to stop): ').lower()
        if another != 'y':
            break

# Asking the user for the number of rooms/size
def numRooms():
    while True:
        try:
            num_rooms = int(input("How many rooms will be painted: "))
            if num_rooms < 1:
                print("Number of rooms cannot be less than 1.")
                continue
            
            total_square_feet = 0
            for i in range(1, num_rooms + 1):
                print(f"Please enter the height and length of one wall for room #{i}")
                height = float(input("Height of wall: "))
                length = float(input("Length of wall: "))
                
                if height <= 0 or length <= 0:
                    print("Square footage cannot be zero or negative.")
                    continue
                
                square_feet = height * length * 2
                total_square_feet += square_feet

            return num_rooms, total_square_feet

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def paintPrice():
    while True:
        try:
            price = float(input("Please enter the price per gallon of the paint (minimum $22.50): "))
            if price < 22.50:
                print("The price of the paint cannot be less than $22.50.")
            else:
                return price
        except ValueError:
            print("Invalid input. Please enter a valid price.")

def calcCost(total_square_feet, price_per_gallon):
    GALLON_COVERAGE = 269
    LABOR_HOURS_PER_GALLON = 2.75
    LABOR_RATE_PER_HOUR = 39.25

    # Calculate and display gallons of paint required, hours of labor required, cost of the paint, labor cost, and total cost of the job

    gallons_required = -(-total_square_feet // GALLON_COVERAGE)
    hours_required = gallons_required * LABOR_HOURS_PER_GALLON
    paint_cost = gallons_required * price_per_gallon
    labor_cost = hours_required * LABOR_RATE_PER_HOUR
    total_cost = paint_cost + labor_cost

    return gallons_required, hours_required, paint_cost, labor_cost, total_cost

def printResults(total_square_feet, gallons_required, hours_required, paint_cost, labor_cost, total_cost):
    print(f"\nSquare feet to be painted: {total_square_feet:,.2f}")
    print(f"Gallons of paint required: {gallons_required}")
    print(f"Paint cost is: ${paint_cost:,.2f}")
    print(f"Labor hours are: {hours_required:.2f}")
    print(f"Labor cost is: ${labor_cost:,.2f}")
    print(f"Total job cost is: ${total_cost:,.2f}\n")

# Running the program
if __name__ == "__main__":
    main()