import requests
import csv
import sqlite3

conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_id (
        id INTEGER PRIMARY KEY,
        name TEXT,
        cca2 TEXT,
        ccn3 TEXT,
        cca3 TEXT,
        cioc TEXT,
        region TEXT,
        subregion TEXT
    )
""")

unique_countries = set()

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/manufacturers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        make, country, year = row
        unique_countries.add(country)

unique_countries.remove('Hong Kong')
unique_countries.add('GB')
unique_countries.remove('UK')

for country in unique_countries:
    # Name, cca2, ccn3, cca3, cioc, region, subregion
    response = requests.get(f'https://restcountries.com/v3.1/name/{country}')

    if response.status_code == 200:
        data = response.json()
        
        cname = data[0]['name']['common']
        cca2 = data[0]['cca2']
        ccn3 = data[0]['ccn3']
        cca3 = data[0]['cca3']
        cioc = data[0]['cioc']
        region = data[0]['region']
        subregion = data[0]['subregion']

        cursor.execute("INSERT INTO country_id (name, cca2, ccn3, cca3, cioc, region, subregion) VALUES (?, ?, ?, ?, ?, ?, ?)", (cname,
                cca2,
                ccn3,
                cca3,
                cioc,
                region,
                subregion))
        
        print(data[0]['name']['common'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

conn.commit()
conn.close()