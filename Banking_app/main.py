"""
Simple CLI for the banking application.
Run this module to start the app:
python -m banking_app.main
"""

import bankcore, accounts


def prompt_main_menu():
    print("\nWelcome to Talha Bank Ltd.")
    print("1. Login to the account")
    print("2. Create an account")
    print("3. Exit")
    return input("Select option (1/2/3): ").strip()


def prompt_logged_menu(customer_id):
    name = bankcore.get_name(customer_id)
    print(f"\nLogged in as {name} ({customer_id})")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Logout")
    return input("Choose (1/2/3/4): ").strip()


def create_account_flow():
    print("\n=== Create Account ===")
    name = input("Enter your full name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    password = input("Set a password: ").strip()
    customer_id = bankcore.create_account(name=name, password=password)
    # ensure balance record initialized
    accounts.balance_record.setdefault(customer_id, 0.0)
    print(f"Account created successfully! Your customer ID is: {customer_id}")
    print("Please note your customer ID and use it to login.")


def login_flow():
    print("\n=== Login ===")
    customer_id = input("Enter customer ID (e.g., 2057-1): ").strip()
    password = input("Enter password: ").strip()
    if bankcore.login(customer_id, password):
        print("Login successful.")
        return customer_id
    else:
        print("Invalid login.")
        return None


def logged_in_session(customer_id):
    while True:
        choice = prompt_logged_menu(customer_id)
        if choice == "1":
            bal = accounts.check_balance(customer_id)
            print(f"Current balance: {bal:.2f}")
        elif choice == "2":
            amt = input("Enter deposit amount: ").strip()
            try:
                new_bal = accounts.deposit(customer_id, float(amt))
                print(f"Deposit successful. New balance: {new_bal:.2f}")
            except Exception as e:
                print("Error:", e)
        elif choice == "3":
            amt = input("Enter withdrawal amount: ").strip()
            try:
                new_bal = accounts.withdraw(customer_id, float(amt))
                print(f"Withdrawal successful. New balance: {new_bal:.2f}")
            except Exception as e:
                print("Error:", e)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option. Choose 1-4.")


def main():
    print("=== Talha Bank CLI===")
    while True:
        choice = prompt_main_menu()
        if choice == "1":
            customer_id = login_flow()
            if customer_id:
                # ensure balance record exists for user
                accounts.balance_record.setdefault(customer_id, 0.0)
                logged_in_session(customer_id)
        elif choice == "2":
            create_account_flow()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
