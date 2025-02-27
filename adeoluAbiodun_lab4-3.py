def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime_status(num):
    """Display whether the number is prime or composite."""
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")

def populate_list(n):
    """Populate a two-dimensional list with integers from 2 to n."""
    return [[i] for i in range(2, n + 1)]

def main():
    """Main function to execute the program."""
    while True:
        try:
            number = int(input("Enter an integer greater than 25: "))
            if number <= 25:
                print("The number must be greater than 25. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    num_list = populate_list(number)
    
    for sublist in num_list:
        for num in sublist:
            display_prime_status(num)

if __name__ == "__main__":
    main()
