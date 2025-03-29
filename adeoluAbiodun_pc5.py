# Name: Adeolu Abiodun  ||  Date: 03/15/2025  ||  Program file: adeoluAbiodun_pc5.py

# This modular Python program checks the validity of passwords input by user, and display valid password(s).

import re

def is_valid_password(password):
    if (6 <= len(password) <= 12 and re.search(r'[a-z]', password) and  re.search(r'[A-Z]', password)
        and re.search(r'\d', password) and re.search(r'[$#@]', password)):
        return True
    return False

def get_valid_passwords(password_list):
    return [pwd for pwd in password_list if is_valid_password(pwd)]

# Here is the main function
def main():
    while True:
        user_input = input("Enter up to 5 passwords, each separated by a comma: ")
        password_list = [pwd.strip() for pwd in user_input.split(",")]

        if not (3 <= len(password_list) <= 5):
            print("Error: Kindly enter between 3 to 5 passwords")
            continue

        valid_passwords = get_valid_passwords(password_list)

        if valid_passwords:
            print(f"Valid passwords are: {', '.join(valid_passwords)}")
        else:
            print("No valid passwords found.")

        # Ask user if they want to run again
        run_again = input("Run again? 1=yes or press ENTER to end program: ")
        if run_again != '1':
            print("Thank you and have a nice day.")
            break

if __name__ == "__main__":
    main()