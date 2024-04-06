import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Jane Smith", "jane@example.com"))

# Commit the changes
conn.commit()

# Query the data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

# Close the connection
conn.close()