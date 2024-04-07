import csv
import sqlite3

conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER,
        brand TEXT,
        model TEXT,
        year INTEGER,
        color TEXT,
        mileage INTEGER,
        price INTEGER,
        location TEXT
    )
""")

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/cars.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        car_id, brand, model, year, color, mileage, price, location = row
        cursor.execute("INSERT INTO cars (id, brand, model, year, color, mileage, price, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (car_id, brand, model, year, color, mileage, price, location))

conn.commit()
conn.close()