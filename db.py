import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop',
        database='bankmanagementsystem',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def setup_database():
    conn = None
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
                balance INT DEFAULT 0
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                account_id INT,
                type VARCHAR(50),
                amount INT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES customers(account_id)
            )
        ''')

        conn.commit()

    except Exception as e:
        print(f"❌ Database setup error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
