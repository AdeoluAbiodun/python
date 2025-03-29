# Name: Adeolu Abiodun  ||  Date: 03/13/2025  ||  Program file: adeoluAbiodun_lab11-2.py

'''This Python program creates a Person superclass, and a subclass, Customer.
It demonstrates an instance of the Customer class and prompts user to enter customer information.'''

# Here is the superclass Person
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# Here is the subclass Customer
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list  # Boolean value (either True or False)


def main():
    customer1 = Customer("Adeolu Abiodun", "999 Providence Rd, Charlotte, NC28212", "987-654-3210", "123ABC", True)

    # Display customer details
    print()
    print("Customer Information:")
    print("===========================")
    print(f"Name: {customer1.name}")
    print(f"Address: {customer1.address}")
    print(f"Phone: {customer1.phone}")
    print(f"Customer Number: {customer1.customer_number}")
    print(f"Mailing List: {'Yes' if customer1.mailing_list else 'No'}")
    
    print()
    print("Enter the customer information below")
    print("================================")

    cust_name = input("Name: ")
    cust_phone = input("Phone No.: ")
    cust_address = input("Address: ")
    cust_no = input("Customer Number: ")
    

    # Validate mailing list input
    while True:
        cust_mailing_list = input("Mailing List (1 for Yes, 2 for No): ").strip()
        if cust_mailing_list == "1":
            cust_mailing_list = True
            break
        elif cust_mailing_list == "2":
            cust_mailing_list = False
            break
        else:
            print("Invalid input! Please enter 1 for Yes or 2 for No.")

    # Customer instance with user input
    customer2 = Customer(cust_name, cust_address, cust_phone, cust_no, cust_mailing_list)
    
    print()
    # Display the entered customer details
    print("Below is the customer's information:")
    print("===============================")
    print(f"Name: {customer2.name}")
    print(f"Address: {customer2.address}")
    print(f"Phone: {customer2.phone}")
    print(f"Customer Number: {customer2.customer_number}")
    print(f"Mailing List: {'Yes' if customer2.mailing_list else 'No'}")


if __name__ == "__main__":
    main()