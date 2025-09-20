from db import setup_database
from service import BankService

def main():
    setup_database()
    bank = BankService()

    while True:
        print("\n🏦 Bank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            password = input("Password: ")
            bank.create_account(name, email, phone, password)

        elif choice == "2":
            try:
                acc_id = int(input("Account ID: "))
                amt = int(input("Amount: "))
                bank.deposit(acc_id, amt)
            except ValueError:
                print("❌ Invalid input. Please enter whole numbers only.")

        elif choice == "3":
            try:
                acc_id = int(input("Account ID: "))
                amt = int(input("Amount: "))
                bank.withdraw(acc_id, amt)
            except ValueError:
                print("❌ Invalid input. Please enter whole numbers only.")

        elif choice == "4":
            try:
                acc_id = int(input("Account ID: "))
                bank.check_balance(acc_id)
            except ValueError:
                print("❌ Invalid Account ID.")

        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
