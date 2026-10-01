import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=StoreDB;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

print("Connected to SQL Server successfully!")

cursor.execute("SELECT * FROM Products")

for product in cursor.fetchall():
    print(product)

connection.close()