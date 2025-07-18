import sqlite3

#Connecting to the database
connection = sqlite3.connect('practice5.db')
cursor = connection.cursor()

#Create the tables
cursor.execute("DROP TABLE IF EXISTS Item")
cursor.execute("DROP TABLE IF EXISTS Customer")

cursor.execute("CREATE TABLE Item('ItemID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Name' TEXT, 'Amount' REAL)")
cursor.execute("CREATE TABLE Customer('CustomerID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Name' TEXT, 'Phone' INTEGER)")

#Insert data into the table
cursor.execute("INSERT INTO Item(Name, Amount) VALUES('Palm Oil', 11.50), ('Honey Beans', 8.15), ('Pound Yam', 10.20), ('Okro', 3)")
cursor.execute("INSERT INTO Customer(Name, Phone) VALUES('Ramsey Tom', 8620001234), ('Nikey Mice', 9993210000), ('Tom Pink', 9801234321)")


query1 = cursor.execute("SELECT * FROM Item")
print("\nHere are the available data in the Item table")
print("_______________________________________________")
for row in query1:
    print(row)

print("\nHere are all customer with 'Tom' in their names in the Customer table")
print("________________________________________________")

query2 = cursor.execute("SELECT * FROM Customer WHERE Name like '%Tom%'")
for line in query2:
    print(line)

connection.commit()

connection.close()