from db import get_connection

class BankService:
    def create_account(self, name, email, phone, password):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO customers (name, email, phone, password) VALUES (?, ?, ?, ?)",
                           (name, email, phone, password))
            conn.commit()
            print("✅ Account created successfully!")
        except Exception as e:
            print("❌ Error:", e)
        finally:
            conn.close()

    def deposit(self, account_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, 'deposit', ?)",
                       (account_id, amount))
        conn.commit()
        conn.close()
        print(f"✅ Deposited {amount} successfully!")

    def withdraw(self, account_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM customers WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        if row and row[0] >= amount:
            cursor.execute("UPDATE customers SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
            cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, 'withdraw', ?)",
                           (account_id, amount))
            conn.commit()
            print(f"✅ Withdrawn {amount} successfully!")
        else:
            print("❌ Insufficient balance or account not found.")
        conn.close()

    def check_balance(self, account_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM customers WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            print(f"💰 Current Balance: {row[0]}")
        else:
            print("❌ Account not found.")
