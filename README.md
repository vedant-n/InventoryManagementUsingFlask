# InventoryManagementUsingFlask
A web-based inventory management system built using Flask (Python), HTML/CSS, and MySQL. It allows businesses to manage stock, track items, and monitor inventory status in real-time through an intuitive and user-friendly dashboard.

## 🔧 Features

- ✅ User Login & Session Management
- 📋 Add New Products
- 🔍 Search & View Products
- ✏️ Edit or Delete Product Entries *(optional extension)*
- 📉 Low Stock Alerts *(optional extension)*
- 🌐 Responsive Design with CSS
- 🛡️ Basic Input Validation

---

## 🛠️ Tech Stack

| Layer       | Tools / Frameworks                 |
|-------------|------------------------------------|
| 🧠 Backend   | Python, Flask                      |
| 💾 Database  | MySQL                              |
| 🎨 Frontend  | HTML5, CSS3                        |
| 🧰 Libraries | Flask, MySQL Connector (`mysql-connector-python`) |

---

## 📂 Project Structure

Inventory-Management-System/
│
├── static/ # CSS files
│ └── style.css
│
├── templates/ # HTML pages
│ ├── login.html
│ ├── dashboard.html
│ └── add_product.html
│
├── app.py # Main Flask application
├── db_setup.sql # SQL script to set up MySQL DB

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system

### 2. Set Up MySQL Database
Open MySQL and create a database:

CREATE DATABASE inventorydb;
USE inventorydb;
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

mydb = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="inventorydb"
)

### 3.  Run the App

python app.py
