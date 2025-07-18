# Name: Adeolu Abiodun  ||  Date: 04/15/2025  ||  Program file: adeoluAbiodun_lab14-1.py

'''This program creates a SQLite database called student_info.db that stores details like the student's name, their major, and
the department they're part of. You can add, view, update, or delete data for students, majors, and departments through an interactive menu.'''


import sqlite3

def connect():
    conn = sqlite3.connect("student_info.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def initialize_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Majors (
        MajorID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL UNIQUE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
        DeptID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL UNIQUE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        MajorID INTEGER,
        DeptID INTEGER,
        FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
        FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
    )''')

    conn.commit()
    conn.close()

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