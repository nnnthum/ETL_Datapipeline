import mysql.connector
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_connection():
    """เชื่อมต่อ MySQL และคืนค่า connection object"""
    logging.info(" Connecting to MySQL database...")
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql'),
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DB', 'sales_db')
    )

def create_table():
    """สร้างตาราง sales ถ้ายังไม่มี"""
    logging.info("🛠Creating table if not exists...")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255),
            price DECIMAL(10,2),
            quantity INT,
            sale_date DATE,
            total_price DECIMAL(10,2)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
    logging.info("Table check completed!")
