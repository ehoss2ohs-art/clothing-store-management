# Clothing Store Management System

A simple console-based system for managing a clothing store's inventory and sales, built with **Python** and **SQL Server**.

## Features

- View all products in stock
- Add new products (name, price, quantity)
- Search for products by name
- Sell products with automatic stock deduction
- Validation: prevents selling more than the available quantity
- Every sale is recorded in a `Sales` table

## Tech Stack

- Python 3
- SQL Server (T-SQL)
- pyodbc

## Database Setup

Run this in SQL Server Management Studio (SSMS):

```sql
CREATE DATABASE StoreDB;
GO
USE StoreDB;
GO

CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL
);

CREATE TABLE Sales (
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL FOREIGN KEY REFERENCES Products(ProductID),
    QuantitySold INT NOT NULL,
    SaleDate DATETIME DEFAULT GETDATE()
);
```

## Installation & Run

1. Install the requirements:
   ```bash
   pip install pyodbc
   ```
2. Install **ODBC Driver 17 for SQL Server**.
3. Create the database using the script above.
4. Run the program:
   ```bash
   python main.py
   ```

## Usage

```
===== STORE MANAGEMENT SYSTEM =====
1. Show Products
2. Add Product
3. Search Product
4. Sell Product
5. Exit
```

## Future Improvements

- Sales reports (daily / monthly revenue)
- Low-stock alerts
- Delete / update products
- GUI or web interface

## Author

**Hussein Junaidy Hussein**
[LinkedIn](https://linkedin.com/in/hussein-geindy-951b6137b)
