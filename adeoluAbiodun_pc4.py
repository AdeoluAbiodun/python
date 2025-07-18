# Name: Adeolu Abiodun  ||  Date: 01/30/2025  ||  Program file: adeoluAbiodun_pc4.py

'''This is a modular Python program that read comma-separated numbers into a list, and
display the square of each of the odd numbers.
'''

#Here is the function to prompt user for inputs and convert the inputs to integers.
def get_values():
    values = input("Enter values separated by a comma: ")
    return [int(number.strip()) for number in values.split(',')]


#Here is the function returning a list of odd numbers
def odd_Numbers(values):
    return [number for number in values if number % 2 != 0]

#Here is a function for finding the square numbers
def square_Numbers(numbers):
    return [number ** 2 for number in numbers]


def main():
    while True:
        values = get_values()
        odd_numbers = odd_Numbers(values)
        squared_odds = square_Numbers(odd_numbers)
        
        print()
        print(f"The odd numbers are: {','.join(map(str, odd_numbers))}")
        print(f"The odd numbers squared are: {','.join(map(str, squared_odds))}")
        
        print()
        to_continue = input("Run again? Enter 1=yes to continue or any other button to abort the program: ")
        if to_continue != '1':
            break

if __name__ == "__main__":
    main()