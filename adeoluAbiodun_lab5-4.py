# Name: Adeolu Abiodun  ||  Date: 09/11/2024  ||  Program file: adeoluAbiodun_lab5-4.py

# Program Description/Purpose: This program creates a modular python that uses turtle graphics to display a snowman.


import random

def generate_random_numbers(count):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(1, 500))
    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_average(numbers):
    total = calculate_total(numbers)
    average = total / len(numbers)
    return average

def find_highest_number(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

def find_lowest_number(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

def display_results(numbers, total, average, highest, lowest):
    print("Numbers generated:", " ".join(map(str, numbers)))
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest number: {highest}")
    print(f"Lowest number: {lowest}")

def main():
    count = int(input("How many random numbers should be written to the file? "))
    filename = "myRandomNumbers.txt"
    
    random_numbers = generate_random_numbers(count)
    write_numbers_to_file(filename, random_numbers)
    
    numbers_from_file = read_numbers_from_file(filename)
    
    total = calculate_total(numbers_from_file)
    average = calculate_average(numbers_from_file)
    highest = find_highest_number(numbers_from_file)
    lowest = find_lowest_number(numbers_from_file)
    
    display_results(numbers_from_file, total, average, highest, lowest)

if __name__ == "__main__":
    main()
