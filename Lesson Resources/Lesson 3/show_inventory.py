import sqlite3
conn = sqlite3.connect('car_showroom.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM inventory WHERE make = 'Ford' AND model_year BETWEEN 2022 AND 2024 and colour = 'Green' and price > 10000")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
