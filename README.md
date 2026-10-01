# clothing-store-management
Simple Clothing Store Management System using Python and SQL Server


import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=StoreDB;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()


def show_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    print("\n--- Products ---")

    for product in products:
        print(
            f"ID: {product.ProductID} | "
            f"Name: {product.ProductName} | "
            f"Price: {product.Price} | "
            f"Quantity: {product.Quantity}"
        )


def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    cursor.execute(
        "INSERT INTO Products (ProductName, Price, Quantity) VALUES (?, ?, ?)",
        name, price, quantity
    )

    connection.commit()
    print("Product added successfully!")


def search_product():
    name = input("Enter product name: ")

    cursor.execute(
        "SELECT * FROM Products WHERE ProductName LIKE ?",
        "%" + name + "%"
    )

    products = cursor.fetchall()

    for product in products:
        print(
            f"ID: {product.ProductID} | "
            f"Name: {product.ProductName} | "
            f"Price: {product.Price} | "
            f"Quantity: {product.Quantity}"
        )
def sell_product():
    product_id = int(input("Enter product ID: "))
    quantity_sold = int(input("Quantity sold: "))

    cursor.execute(
        "SELECT Quantity FROM Products WHERE ProductID = ?",
        product_id
    )

    product = cursor.fetchone()

    if product is None:
        print("Product not found!")
        return

    if product.Quantity < quantity_sold:
        print("Not enough quantity!")
        return

    # تسجيل عملية البيع
    cursor.execute(
        "INSERT INTO Sales (ProductID, QuantitySold) VALUES (?, ?)",
        product_id, quantity_sold
    )

    # تقليل الكمية من المخزن
    cursor.execute(
        "UPDATE Products SET Quantity = Quantity - ? WHERE ProductID = ?",
        quantity_sold, product_id
    )

    connection.commit()

    print("Sale completed successfully!")
    

while True:

    print("\n===== STORE MANAGEMENT SYSTEM =====")
    print("1. Show Products")
    print("2. Add Product")
    print("3. Search Product")
    print("4. Sell Product")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        search_product()

    elif choice == "4":
        sell_product()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


connection.close()
