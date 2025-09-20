import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='bank_db'
    )

def setup_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                account_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(20),
                password VARCHAR(255) NOT NULL,
                balance DECIMAL(10, 2) DEFAULT 0.00
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                account_id INT,
                type VARCHAR(50),
                amount DECIMAL(10, 2),
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES customers(account_id)
            )
        ''')

        conn.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

setup_database()
