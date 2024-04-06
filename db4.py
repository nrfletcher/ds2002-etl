import requests
import csv
import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
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

# Name, cca2, ccn3, cca3, cioc, region, subregion
response = requests.get("https://restcountries.com/v3.1/name/GB")

if response.status_code == 200:
    data = response.json()
    
    for d in data:
        for f in d:
            print(f'Type: {f} Val: {d[f]}')
else:
    print(f"Error: {response.status_code} - {response.text}")