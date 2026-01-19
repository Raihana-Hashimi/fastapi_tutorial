import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER,
        content TEXT,
        weight REAL,
        status TEXT
    )
""")

cursor.execute("""
    INSERT INTO shipment
    VALUES (12702, "basalt", 18.5, "in transit")
""")
connection.commit()

connection.close()