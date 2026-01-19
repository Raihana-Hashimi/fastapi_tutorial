import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER PRIMARY KEY,
        content TEXT,
        weight REAL,
        status TEXT
    )
""")

# cursor.execute("DROP TABLE shipment")
# connection.commit()

# cursor.execute("""
#     INSERT INTO shipment
#     VALUES (12701, "basalt", 18.5, "in transit")
# """)
# connection.commit()

# cursor.execute("""
#     SELECT * FROM shipment
#     WHERE id = 12702
# """)
# result = cursor.fetchone()
# print(result)
id = 12701
status = "Out_for_delivery"

cursor.execute("""
    UPDATE shipment SET status = :status WHERE id = :id
""",
    {"status": status, "id": id}
)
connection.commit()

# cursor.execute("""
#     DELETE FROM shipment
# """)
# connection.commit()


connection.close()