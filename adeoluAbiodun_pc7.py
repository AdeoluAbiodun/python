# Name: Adeolu Abiodun  ||  Date: 04/15/2025  ||  Program file: adeoluAbiodun_pc7.py

import sqlite3

'''# Use forward slashes (safe for Windows) or raw string
import os

print(os.path.exists('C:/Users/ADEOLU T. ABIODUN/OneDrive/Documents/school/CSC121/CSC221'))'''


import sqlite3

# Make sure the file path is correctly formatted
db_path = 'C:/Users/ADEOLU T. ABIODUN/OneDrive/Documents/school/CSC121/CSC221/student_info.db'

# Connect to the database
connection = sqlite3.connect(db_path)
cur = connection.cursor()

# Create Majors table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Majors (
        MajorID INTEGER PRIMARY KEY,
        Name TEXT
    );
''')

# Create Departments table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        DeptID INTEGER PRIMARY KEY,
        Name TEXT
    );
''')

# Create Students table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        MajorID INTEGER,
        FOREIGN KEY (MajorID) REFERENCES Majors(MajorID)
    );
''')

# Save (commit) and close
connection.commit()
connection.close()

print("Database created and tables initialized successfully.")

