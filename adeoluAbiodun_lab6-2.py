# Name: Adeolu Abiodun  ||  Date: 09/19/2024  ||  Program file: adeoluAbiodun_lab6-2.py

# Program Description/Purpose: This program read a file and calculate the average of the numbers in the file.
import os

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = []
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid number and will be ignored.")
            return numbers
    except IOError:
        print(f"Error: The file '{file_path}' could not be found or opened.")
        return None

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    file_path = input("Enter the full path of the file to read (e.g., C:\\Users\\Adeolu T. Abiodun\\Downloads\\exceptionNumbers.txt): ")
    if os.path.exists(file_path):
        numbers = read_numbers_from_file(file_path)
        if numbers is not None:
            average = calculate_average(numbers)
            if average is not None:
                print(f"The average of the numbers in the file is: {average:.2f}")
            else:
                print("No valid numbers found in the file to calculate an average.")
        else:
            print("No numbers to process due to file read error.")
    else:
        print(f"Error: The file path '{file_path}' does not exist.")

if __name__ == "__main__":
    main()
