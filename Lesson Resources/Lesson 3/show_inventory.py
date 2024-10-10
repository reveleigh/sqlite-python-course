import sqlite3
conn = sqlite3.connect('car_showroom.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM inventory")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
