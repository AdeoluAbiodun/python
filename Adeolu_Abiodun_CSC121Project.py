'''
# Name: Adeolu Abiodun  ||  Date: 9/27/2024  ||  Program file: Adeolu_Abiodun_CSC121Project

# Program Description/Purpose: This Python program generates a cellular telephone bill, accepts cash payment, and instruct the cashier on how to provide the correct change.

# Constants for skate prices and tax rate
ROLLER_SKATES_PRICE_1_4 = 154.75
ROLLER_SKATES_PRICE_5_PLUS = 137.50
ROLLER_BLADES_PRICE_1_4 = 229.95
ROLLER_BLADES_PRICE_5_PLUS = 188.95
SALES_TAX_RATE = 0.0675

# Function to display the menu
def display_menu():
    print("1. Roller Skates")
    print("2. Roller Blades")
    print()

# Function to get the user's skate choice and validate input
def get_skate_choice():
    while True:
        try:
            choice = int(input("Enter choice of skates (1 for Roller Skates, 2 for Roller Blades): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

# Function to get the number of pairs and validate input
def get_number_of_pairs():
    while True:
        try:
            number_of_pairs = int(input("How many pairs of skates are you buying? "))
            if number_of_pairs >= 1:
                return number_of_pairs
            else:
                print("You must buy at least 1 pair of skates.")
        except ValueError:
            print("Invalid input. Please enter a valid number of pairs.")

# Function to calculate the subtotal based on skate type and number of pairs
def calculate_subtotal(choice, number_of_pairs):
    if choice == 1:  # Roller Skates
        if number_of_pairs <= 4:
            return number_of_pairs * ROLLER_SKATES_PRICE_1_4
        else:
            return number_of_pairs * ROLLER_SKATES_PRICE_5_PLUS
    elif choice == 2:  # Roller Blades
        if number_of_pairs <= 4:
            return number_of_pairs * ROLLER_BLADES_PRICE_1_4
        else:
            return number_of_pairs * ROLLER_BLADES_PRICE_5_PLUS

# Function to calculate sales tax
def calculate_tax(subtotal):
    return subtotal * SALES_TAX_RATE

# Function to display the results with proper formatting
def display_results(choice, number_of_pairs, subtotal, tax, total):
    skate_type = "Roller Skates" if choice == 1 else "Roller Blades"
    print(f"\nThe customer purchased {number_of_pairs} pair(s) of {skate_type}.")
    print(f"The cost is           ${subtotal:,.2f}")
    print(f"The sales tax is      ${tax:,.2f}")
    print(f"The total charge is   ${total:,.2f}")
# Main function to run the program
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


my_sentence = "This is a beautiful day. Thank God"

new_sentence = input("Enter one word here: ")

position = my_sentence.find(new_sentence)

while position >= 1:
    print(f'"{new_sentence}" is located in {position}th position of "{my_sentence}".')
    new_sentence = input("Enter one word here: ")

print("Oh no, You can't use 'This' in your sentence." + "\nHere is the end of the program")



mystr = 'yes'


yourstr = 'no'


mystr += yourstr * 2


print(mystr)



i = 3


pattern = 'z' * (5 * i)
print(pattern)


string = 'abcd'


print(string.upper())


password = 'ILOVEPYTHON'


if password.isalpha():


print('Invalid, must contain one number.')


elif password.isdigit():


print('Invalid, must have one non-numeric character.')


elif password.isupper():


print('Invalid, cannot be all uppercase characters.')


else:


print('Your password is secure!')



string[i] = 'i'



about = "I am a dedicated, enthusiastic and strategic analyst with over 7years work experience as a Business Analyst in various industries like communication, manufacturing and banking. I have in-depth knowledge of SQL, Microsoft Excel, Microsoft Access, Tableau, data cleaning, data visualization, data presentation, data warehousing, data mining, CSS, HTML and Python. I work well with/without supervision and I'm a team player."

new_about = about.replace("7", "ten (10) ")
print(new_about)



# password = input("Enter your password here: ")

new_password = "myLogin"

for ch in new_password:
    print(ch)

print("Error out")



# This program accepts a password from the user and tests if the password meets the following criteria:
# a. Is at least 12 characters long.
# b. Contains 1 or more uppercase letters.
# c. Contains 1 or more lowercase letters.
# d. Contains 1 or more numeric digits.

# password = input("Enter your password here: ") # Accept password input from user

def valid_password(password):
    #Declare the Boolean variables
    password_length = False
    password_upper = False
    password_lower = False
    password_digit = False

    if len(password) >= 7:
        password_length = True
    
    for ch in password:
        if ch.isupper():
            password_upper = True
        
        if ch.islower():
            password_lower = True

        if ch.isdigit():
            password_digit = True
            
    
    if password_length and password_upper and password_lower and password_digit:
        print("Great! Your password is valid.")
    else:
        print("Invalid passord.")
   
if __name__ == "__main__":
    password = input("Enter your password here: ") 
    valid_password(password)


import math

def calculate_q(d_values, c=50, h=30):
    """Calculate Q for a list of D values using the formula."""
    return [round(math.sqrt((2 * c * d) / h)) for d in d_values]

def parse_input(input_string):
    """Parse a comma-separated string into a list of floats."""
    try:
        return [float(value) for value in input_string.split(",")]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return []

def main():
    """Main function to handle user input and program execution."""
    while True:
        # Get input from user
        input_string = input("Enter your numbers separated by a comma: ")
        
        # Parse input into a list of numbers
        items = parse_input(input_string)

        # Only proceed if the input is valid
        if items:
            # Calculate Q values
            value = calculate_q(items)

            # Display calculated values
            print("The calculated values are: ", ", ".join(map(str, value)))

        # Ask if the user wants to run again
        choice = input("Run program again? 1 = yes or press ENTER to stop: ")
        if choice.strip() != "1":
            break

if __name__ == "__main__":
    main()


# This modular Python program prompts user for input, calculates a value using the formula (Q = Square root of [(2 * C * D)/H]), and then displays the result

import math

def calculate_Q(D_values):
    # Calculates the Q values using the formula: Q = Square root of [(2 * C * D) / H]
    # Constants: C = 50 and H = 30
    C = 50
    H = 30
    result = []
    for D in D_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(round(Q))
    return result

def parse_input(input_string): # Takes a string of comma-separated numbers and converts it into a list of floats.
    
    try:
       return [float(value) for value in input_string.split(",")]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return []

# Below is the main function that controls the program. It asks the user for input, calculates Q values, and displays the results.
# The program will keep running until the user decides to stop.
def main():
    while True:
        input_string = input("Enter your numbers separated by a comma: ")


        items = parse_input(input_string)

        if items:
            value = calculate_Q(items)

            print("The calculated values are: ", ", ".join(map(str, value)))

        
        choice = input("Would you like to run the program again? Enter 1 for yes or any other key to exit: ") # Ask user if they want to run the program again.
        if choice.strip() != "1":
            print("Thank you and Goodbye!")
            break

if __name__ == "__main__":
    main()

def main():
    month = "May June July August September"
    date = "1;2;3;4;5;6;7;8;9"

    display_tokens(month, " ")
    print()

    display_tokens(date, ";")
    print()


def display_tokens(data, delimiter):
    tokens = data.split(delimiter)

    for item in tokens:
        print(f"Token: {item}")

if __name__ == "__main__":
    main()


# This program separate and display main numbers in the days

def main():
    today = "1/26/2025"
    new_today(today, "/")
    print()

def new_today(data, delimiter):
    duration = data.split(delimiter)
    for character in duration:
        print(f"today is: {character}")

if __name__ == "__main__":
    main()



def convert_to_pig_latin(sentence):
    """Convert a sentence to upper-case Pig Latin."""
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        # Move the first letter to the end, add 'ay', and convert to upper case
        pig_latin_word = (word[1:] + word[0] + 'ay').upper()
        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)

# Main loop
while True:
    user_input = input("Enter a string or press enter to stop the program: ")

    # Exit the loop if the user presses enter
    if user_input.strip() == "":
        print("Program stopped. Goodbye!")
        break

    # Convert the input to Pig Latin and display the result
    pig_latin_output = convert_to_pig_latin(user_input)
    print("Your input converted to upper-case pig latin is as follows:")
    print(pig_latin_output)
    print()


word = input("Enter a word to play pig-latin or press enter to abort: ").strip()

#word = user.strip()

if not word:
    new_word = word[1:]
    slide_word = word[0]
    print((f"The pig-latin word is: {new_word}" + f"{slide_word}" + f"ay").strip())
        
    else:
        print("Invalid value.")
        break
    word = input("Enter a word to play pig-latin or press enter to abort: ")
    
        
print("Program aborted")


   

team = {"Goal keeper": "Jimmy", "Defender 1": "Timothy", "Defender 2": "James", "Mid fielder 1": "Tom", "Mid fielder 2": "Young", "Striker 1": "Krystal", "Striker 2": "Allen"}

team["coach"] = "Matthew"

team["Goal keeper"] = "Carter"

if len(team) >= 9:
    print("The items are greater/equal to 7")

else:
    print("Fewer items.")


while True:
    value = input("Enter the role you're looking for: ")


    if value == team["Defender 1"]:
        print(f"{value} is the Defender 1")

    elif value == team["Defender 2"]:
        print(f"{value} is the Defender 2")

    elif value == team["Goal keeper"]:
        print(f"{value} is the Goal keeper")
    
    elif value == team["Mid fielder 1"]:
        print(f"{value} is the Mid fielder 1")
    
    
    elif value == team["Mid fielder 2"]:
        print(f"{value} is the Mid fielder 2")

    
    elif value == team["Striker 1"]:
        print(f"{value} is the Striker 1")

    elif value == team["Striker 2"]:
        print(f"{value} is the Striker 2")

    else:
        print(f"{value} is not a member of this team.")
        break

print("Thank you!")



print(team)

'''

adeolu_family = {"Adeolu" : [100, 200, 300], "Lois": 46, "Cathiana": [110, 190, 300]}

#adeolu_family["Lois"] = [105, 210, 300]

key, value = adeolu_family.popitem()

#for key, value in adeolu_family.items():
#    print(key, value)
    #print(f"{key}: {adeolu_family[key]}")

print(key, value)
print(adeolu_family)
