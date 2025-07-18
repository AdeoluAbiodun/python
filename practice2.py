'''This program is to create and display church membership details in an easy to manage format'''

import sqlite3

connection = sqlite3.connect('Church_Membership.db')

cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS church_membership''')
cursor.execute('''CREATE TABLE church_membership("S/N" INTEGER, "Name" TEXT, "Phone_Number" INTEGER)''')

technican = [
                (1, "Tony Brown", 90812345678),
                (2, "James Peter", 8022346542),
                (3, "Goodness Kelly", 3243247860),]

choir = [(10, "Alex Yay", 4025678002),
         (11, "Loius Peterside", 8082316750),]

cursor.executemany('INSERT INTO church_membership VALUES(?,?,?)', technican)
cursor.executemany("INSERT INTO church_membership VALUES(?,?,?)", choir)

cursor.execute("select * from church_membership")

print(cursor.fetchall())

# print(tables)

connection.commit()
connection.close()
