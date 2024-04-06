import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Execute the SQL script
with open('sources/chiptuning.sql', 'r') as f:
    cursor.executescript(f.read())

# Commit the changes and close the connection
conn.close()