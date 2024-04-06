import csv
import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS manufacturers (
        make TEXT,
        country TEXT,
        year INTEGER
    )
""")

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/manufacturers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        make, country, year = row
        cursor.execute("INSERT INTO manufacturers (make, country, year) VALUES (?, ?, ?)", (make, country, year))

conn.commit()
conn.close()