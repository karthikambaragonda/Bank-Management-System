from db import get_connection

class BankService:
    def create_account(self, name, email, phone, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO customers (name, email, phone, password)
                VALUES (%s, %s, %s, %s)
            """, (name, email, phone, password))

            conn.commit()
            cursor.execute("select account_id from customers where email = %s",(email))
            id = cursor.fetchone()
            print("✅ Account created successfully.")
            print(f"You Account id is{id['account_id']}")

        except Exception as e:
            if 'Duplicate entry' in str(e):
                print("❌ Error: Email already exists.")
            else:
                print(f"❌ Error: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

    def deposit(self, account_id, amount):
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT balance FROM customers WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()

            if not result:
                print("❌ Account not found.")
                return

            current_balance = result['balance']
            new_balance = current_balance + amount

            cursor.execute("UPDATE customers SET balance = %s WHERE account_id = %s", (new_balance, account_id))
            cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'deposit', %s)", (account_id, amount))

            conn.commit()
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{new_balance}")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

    def withdraw(self, account_id, amount):
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT balance FROM customers WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()

            if not result:
                print("❌ Account not found.")
                return

            current_balance = result['balance']

            if current_balance < amount:
                print("❌ Insufficient balance.")
                return

            new_balance = current_balance - amount

            cursor.execute("UPDATE customers SET balance = %s WHERE account_id = %s", (new_balance, account_id))
            cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'withdraw', %s)", (account_id, amount))

            conn.commit()
            print(f"✅ Withdrew ₹{amount}. New Balance: ₹{new_balance}")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

    def check_balance(self, account_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT balance FROM customers WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()

            if result:
                print(f"💰 Current Balance: ₹{result['balance']}")
            else:
                print("❌ Account not found.")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
