import sqlite3
# Connect to the database 
db = sqlite3.connect("python_programming.db")
cursor = db.cursor()

# Create the python_programming table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
""")
db.commit()
# Insert new rows
new_rows = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]
cursor.executemany("INSERT INTO python_programming VALUES (1, 2, 3)", new_rows)

# Select records with grade between 60 and 80
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
selected_records = cursor.fetchall()
print("Records with grade between 60 and 80:")
for record in selected_records:
    print(record)

# Update Carl Davis's grade to 65
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")

# Delete Dennis Fredrickson's row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")

# Update grade for students with id greater than 55 to 80
cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")

# Commit changes and close the connection
db.commit()
db.close()

print("Database manipulation completed successfully.")
