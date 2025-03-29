# Name: Adeolu Abiodun  ||  Date: 03/18/2025  ||  Program file: adeoluAbiodun_lab_12-1.py

# This modular Python program accepts two arguments into the parameters x and y and return the value of x times y.

def recursive(x, y):
    if x == 1: 
        return y
    return y + recursive(x - 1, y)

def main():
    try:
        x = int(input("Enter a positive nonzero integer for x: "))
        y = int(input("Enter a positive nonzero integer for y: "))

        if x <= 0 or y <= 0:
            print("Please enter positive integers.")
            return

        value = recursive(x, y)
        print(f"The value of {x} × {y} is: {value}")

    except ValueError:
        print("Invalid input! Please enter integer values.")

if __name__ == "__main__":
    main()
