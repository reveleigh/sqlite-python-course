import sqlite3
  
conn = sqlite3.connect('car_showroom.db')
cursor = conn.cursor()

colour = input("Enter car colour: ").title() 
make = input("Enter car make: ").title()
cursor.execute("SELECT * FROM inventory WHERE colour = ? AND make = ?;", (colour, make))
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()