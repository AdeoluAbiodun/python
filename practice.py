'''
import pickle


setA = {2, 4, 6, 'A', 'C', 'G'}

setB = {4, 8, 'C', 'F'}

setC = setA ^ (setB)

#print(setC.issubset(setA))


#The following program performs mathematical operations on homeowners in two states.

NJ = set(['Terry', 'Cameron', 'James', 'Zella', 'Kelly'])

NY = set(['Sarah', 'Paul', 'Zella', 'Keller', 'Terry', 'Tommy'])

#Find the total owners in both states

total = NJ.union(NY)

with open("total.pkl", "wb") as file:
    pickle.dump(total, file)

print("Here are the total homeowners in the 2 states")
print("......................................")
for name in total:
    print(name)


#Find the homeowners with house(s) in both state.

intersect = NJ.intersection(NY)

print()

print("Here are the homeowners with house(s) in both states")
print("......................................")
for name1 in intersect:
    print(name1)

print()
print()
import pickle

with open("total.pkl", "rb") as file:
    loaded_state = pickle.load(file)

print(loaded_state)




import pickle

myEmployee = {"HR" : "Tonny Robinson",
              "PM" : "Junior Wax",
              "Programmer" : "Henry Thompson",
              "Designer" : "Katrina Paul"}

with open("employee.dat", "wb") as myData:
    pickle.dump(myEmployee, myData)


import pickle
with open("employee.dat", "rb") as employeeDatabase:
    staff = pickle.load(employeeDatabase)

print(staff['PM'])

'''

'''
#This program accept input from user and display the index with the character starting from the last character.

confirmation = "y"

while confirmation == 'y':
    userInput = input("Enter a word here: ")

    wordCount = len(userInput)
    for ch in userInput:
        wordCount -= 1
        print(wordCount, userInput[wordCount])
        
    confirmation = input("Enter y to continue or any other key to stop: ")
   
print("Program ended")

'''
'''

confirmation = "y"

while confirmation == 'y':
    userInput = input("Enter a word here: ")

    wordCount = 0
    for ch in userInput:
        wordCount += 1
        print(wordCount, ch) #userInput[wordCount])
        
    confirmation = input("Enter y to continue or any other key to stop: ")
   
print("Program ended")

'''
'''
count = 0


confirm = "y"

while confirm == "y":
    pick = input("Enter the word here: ")

    find_pick = input("Enter the letter here: ")

    for find_pick in pick:
        count += 1
        print(count, find_pick)
    confirm = input("Do you want to continue: y = yes / any key to abort: ")
    #pick = input("Enter the word here: ")
    #find_pick = input("Enter the letter here: ").lower()
    break
print("Program aborted")
'''
'''
class Building:
    def __init__(self, floor, manager, team_members, parking):
        self.floor = floor
        self.manager = manager
        self.team = team_members
        self.parking = parking
    
    def __str__(self):
        return (f"Building Details:\n"
                f"Floor: {self.floor}\n"
                f"Manager: {self.manager}\n"
                f"Team Members: {self.team}\n"
                f"Parking Lot Info: {self.parking.name}, {self.parking.number_of_cars}, {self.parking.parking_lot}")



class ParkingLot:
    def __init__(self, name, number_of_cars, lot_number):
        self.name = name
        self.number_of_cars = number_of_cars
        self.parking_lot = lot_number




parking1 = ParkingLot("North East Lot", "500 cars", "Lot A1")

parking2 = ParkingLot("South Pole Lot", "725 cars", "Lot X")

building1 = Building("Floor A", "Apostle Paul", "Peter Rabbits, James Bond, Patterson Roberts", parking1)

building2 = Building("Floor N", "Apostle Thomas", "Annie Janet, Markus Tonny, Liu Black", parking2)


print(f"{parking2.name} contains {parking2.number_of_cars}.")

print(f"{parking1.name} contains {parking1.number_of_cars}.")

print()
print()
print()

print(building1)

print("=====================================")
print(building2)

'''
'''
myText = open("C:/Users/ADEOLU T. ABIODUN/Downloads/text.txt")

readFile = myText.read()

myWord = input("Enter your chosen word here: ")

myNumber = len(myWord)

# for myWord in readFile:
print(readFile[0:myNumber])
   #myNumbert = myNumber + 1
   #print(f"The total count of {myWord} in my file is: {myNumber}")
'''

'''

fileInput = input("Enter the file path here: ")
filename = open(fileInput)

counting = filename.count("business")

#for line in filename:

print(counting)
'''

'''
userList = list()

while True:
    user = input("Enter your list here separated by commas: ")

    
    
    if user == "done" : break
    
    newvalue = float(user)

    userList.append(newvalue)

    print(userList)

'''
'''
#accounts.py - here is the module's name

class SavingsAccount:
    def __init__(self, account_number, interest_rate, account_balance):
        self._account_number = account_number
        self._interest_rate = interest_rate
        self._account_balance = account_balance
    
    #Here are the mutators/sets.
    def set_account_number(self,account_number):
        self._account_number = account_number

    def set_interest_rate(self,interest_rate):
        self._interest_rate = interest_rate

    def set_account_balance(self,account_balance):
        self._account_balance = account_balance

    #Here are the accessors/gets.
    def get_account_number(self):
        return self._account_number
    
    def get_interest_rate(self):
        return self._interest_rate
    
    def get_account_balance(self):
        return self._account_balance

class CD(SavingsAccount):
    def __init__(self, account_number, interest_rate, account_balance, maturity_date):
        SavingsAccount.__init__(self, account_number, interest_rate, account_balance)
        self._maturity_date = maturity_date
    
    def set_maturity_date(self, maturity_date):
        self._maturity_date = maturity_date
        
    
    def get_maturity_date(self):
        return self._maturity_date


import practice

def main():

# Define the Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    
    def set_name(self, name):
        self._name = name
    
    def set_address(self, address):
        self._address = address
    
    def set_phone(self, phone):
        self._phone = phone
    

    def get_name(self):
        return self._name
    
    def get_address(self):
        return self._address
    
    def get_phone(self):
        return self._phone
    

    #def __str__(self):
    #    return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}

# Define the Customer class as a subclass of Person
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list  # Boolean value: True or False
    
    def set_customer_number(self, customer_number):
        self._customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self._mailing_list = mailing_list
    
    def get_customer_number(self):
        return self._customer_number
    
    def get_mailing_list(self):
        #mailing_status = "Yes" if self.mailing_list else "No"
        return self._mailing_list

# Demonstrate an instance of the Customer class
def main():
    # Creating a customer instance

    customer1 = Customer("John Doe", "123 Elm St, Springfield", "555-1234", 1001, True)

    print()
    print("Enter the customer information here: ")
    print("=============================")
    #cust_name = input("Name: ")
    #custName = input("Enter name here: ")
    
    #customer = Customer(name, address, phone, customer_number, mailing_list)
    
    #customer2 = 
    # Displaying customer details
    print("Customer Information:")
    print(customer1)

# Run the program
if __name__ == "__main__":
    main()
'''
'''
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

numbers = [1,2,3,4,5,6,7,8,9]

edited = range_sum(numbers, 2, 5)

print(edited)'
'''
'''
import sys

# Define the Ackermann function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Define a safe tester function to warn about recursion limits
def test_ackermann(m, n):
    # Set a threshold to avoid hitting the max recursion depth
    recursion_threshold = 1000  # Python's default recursion limit
    estimated_depth = (2 ** m) * (n + 1)  # rough estimation

    if estimated_depth > recursion_threshold:
        print(f"Warning: The inputs m={m}, n={n} may exceed Python's recursion limit.")
        return None
    else:
        try:
            result = ackermann(m, n)
            print(f"Ackermann({m}, {n}) = {result}")
            return result
        except RecursionError:
            print(f"Error: Recursion limit exceeded for m={m}, n={n}. Try smaller values.")
            return None

# Test the function with small values
if __name__ == "__main__":
    test_ackermann(0, 0)  # Should return 1
    test_ackermann(1, 2)  # Should return 4
    test_ackermann(2, 2)  # Should return 7
    test_ackermann(3, 2)  # Should return 29
    test_ackermann(4, 1)  # Will likely trigger the warning or a RecursionError'
'''

'''
import tkinter

myGUI = tkinter.Tk()

print(myGUI)
'''
'''

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("1st GUI")
        tkinter.mainloop()
if __name__ == "__main__":
    my_gui = myGUI()
'''


'''This modular GUI python program accepts inputs from the user, and 
converts Celsius temperatures to Fahrenheit temperatures 
using the provided formular F = 9/5C + 32'''

'''

import tkinter

class GUI_Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        
        self.top_label = tkinter.Label(self.top_frame, text="Enter a Celsius temperature: ")
        self.entry = tkinter.Entry(self.top_frame, width=10)

        self.top_label.pack(side="left")
        self.entry.pack(side="left")

        self.middle_label = tkinter.Label(self.middle_frame, text="Converted to Fahrenheit: ")
        self.display = tkinter.StringVar()        
        self.input_display = tkinter.Label(self.middle_frame, textvariable=self.display)

        
        self.middle_label.pack(side="left")
        self.input_display.pack(side="left")

        self.bottom_botton = tkinter.Button(self.bottom_frame, text="Convert", command=self.cal_temp, relief="solid")
        self.quit = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy, relief="sunken")

        self.bottom_botton.pack(side="left")
        self.quit.pack(side="left")

        
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def cal_temp(self):

        C = float(self.entry.get())
        F = (9/5) * C + 32

        self.display.set(F)
if __name__ == "__main__":
    GUI_Converter()
        
'''
        
'''

import sqlite3

def main():
    connect = sqlite3.connect(r'C:\Users\ADEOLU T. ABIODUN\OneDrive\Documents\school\CSC121\CSC221\practice.db')
    cur = connect.cursor()

    CREATE TABLE Practice (Number int, Item str, Amount float)

    connect.close()

if __name__ == "__main__":
    main()

'''
 
'''
# -------- Helper Function to Safely Execute DB Action --------
def safe_db_action(action):
    try:
        action()
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    except sqlite3.OperationalError as e:
        print(f"Operational Error: {e}. This usually means the database is locked. Try again shortly.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# -------- Majors --------
def handle_majors():
    while True:
        print("\n--- Majors Menu ---")
        print("1. Add Major")
        print("2. View Majors")
        print("3. Update Major")
        print("4. Delete Major")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        def add_major():
            name = input("Enter major name: ")
            with connect() as conn:
                conn.execute("INSERT INTO Majors (Name) VALUES (?)", (name,))
                conn.commit()
                print("Major added.")

        def view_majors():
            with connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Majors")
                for row in cursor.fetchall():
                    print(row)

        def update_major():
            id = input("Enter Major ID to update: ")
            name = input("Enter new major name: ")
            with connect() as conn:
                conn.execute("UPDATE Majors SET Name = ? WHERE MajorID = ?", (name, id))
                conn.commit()
                print("Major updated.")

        def delete_major():
            id = input("Enter Major ID to delete: ")
            with connect() as conn:
                conn.execute("DELETE FROM Majors WHERE MajorID = ?", (id,))
                conn.commit()
                print("Major deleted.")

        if choice == '1':
            safe_db_action(add_major)
        elif choice == '2':
            safe_db_action(view_majors)
        elif choice == '3':
            safe_db_action(update_major)
        elif choice == '4':
            safe_db_action(delete_major)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# -------- Departments --------
def handle_departments():
    while True:
        print("\n--- Departments Menu ---")
        print("1. Add Department")
        print("2. View Departments")
        print("3. Update Department")
        print("4. Delete Department")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        def add_dept():
            name = input("Enter department name: ")
            with connect() as conn:
                conn.execute("INSERT INTO Departments (Name) VALUES (?)", (name,))
                conn.commit()
                print("Department added.")

        def view_depts():
            with connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Departments")
                for row in cursor.fetchall():
                    print(row)

        def update_dept():
            id = input("Enter Department ID to update: ")
            name = input("Enter new department name: ")
            with connect() as conn:
                conn.execute("UPDATE Departments SET Name = ? WHERE DeptID = ?", (name, id))
                conn.commit()
                print("Department updated.")

        def delete_dept():
            id = input("Enter Department ID to delete: ")
            with connect() as conn:
                conn.execute("DELETE FROM Departments WHERE DeptID = ?", (id,))
                conn.commit()
                print("Department deleted.")

        if choice == '1':
            safe_db_action(add_dept)
        elif choice == '2':
            safe_db_action(view_depts)
        elif choice == '3':
            safe_db_action(update_dept)
        elif choice == '4':
            safe_db_action(delete_dept)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# -------- Students --------
def handle_students():
    while True:
        print("\n--- Students Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        def add_student():
            name = input("Enter student name: ")
            major_id = input("Enter major ID: ")
            dept_id = input("Enter department ID: ")
            with connect() as conn:
                conn.execute("INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)", (name, major_id, dept_id))
                conn.commit()
                print("Student added.")

        def view_students():
            with connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Students")
                for row in cursor.fetchall():
                    print(row)

        def update_student():
            id = input("Enter Student ID to update: ")
            name = input("Enter new student name: ")
            major_id = input("Enter new major ID: ")
            dept_id = input("Enter new department ID: ")
            with connect() as conn:
                conn.execute("UPDATE Students SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID = ?", (name, major_id, dept_id, id))
                conn.commit()
                print("Student updated.")

        def delete_student():
            id = input("Enter Student ID to delete: ")
            with connect() as conn:
                conn.execute("DELETE FROM Students WHERE StudentID = ?", (id,))
                conn.commit()
                print("Student deleted.")

        if choice == '1':
            safe_db_action(add_student)
        elif choice == '2':
            safe_db_action(view_students)
        elif choice == '3':
            safe_db_action(update_student)
        elif choice == '4':
            safe_db_action(delete_student)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# -------- Main Menu --------
def display_menu():
    print("\n----- Student Info Database Menu -----")
    print("1. Manage Majors")
    print("2. Manage Departments")
    print("3. Manage Students")
    print("4. Exit")

def get_menu_choice():
    try:
        choice = int(input("Enter your choice (1-4): "))
        if 1 <= choice <= 4:
            return choice
        else:
            print("Invalid choice. Try again.")
            return get_menu_choice()
    except ValueError:
        print("Invalid input. Enter a number.")
        return get_menu_choice()

def main_menu():
    initialize_database()
    choice = 0
    while choice != 4:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            handle_majors()
        elif choice == 2:
            handle_departments()
        elif choice == 3:
            handle_students()

if __name__ == '__main__':
    main_menu()


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Guess the Number Game</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 50px; }
    input, button { padding: 10px; font-size: 16px; }
    #result { margin-top: 20px; font-weight: bold; }
  </style>
</head>
<body>

  <h1>🎯 Guess the Number!</h1>
  <p>I’m thinking of a number between 1 and 100. Can you guess it?</p>
  <input type="number" id="guess" placeholder="Enter your guess" />
  <button onclick="checkGuess()">Submit</button>
  <p id="result"></p>

  <script>
    let number = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;

    function checkGuess() {
      const guess = parseInt(document.getElementById('guess').value);
      const result = document.getElementById('result');
      attempts++;

      if (guess === number) {
        result.textContent = `🎉 Correct! You guessed it in ${attempts} attempt(s)!`;
      } else if (guess < number) {
        result.textContent = "📉 Too low. Try again!";
      } else if (guess > number) {
        result.textContent = "📈 Too high. Try again!";
      } else {
        result.textContent = "❌ Invalid input.";
      }
    }
  </script>

</body>
</html>
'''
