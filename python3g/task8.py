balance = 1000.0

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print(f"Your balance: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Deposit amount: $"))
        balance += amount
        print(f"New balance: ${balance:.2f}")

    elif choice == "3":
        amount = float(input("Withdraw amount: $"))
        if amount > balance:
            print("Error: Insufficient funds.")
        else:
            balance -= amount
            print(f"New balance: ${balance:.2f}")

    elif choice == "4":
        print("Thank you for using our ATM!")
        break  # This is the only way to exit the loop

    else:
        print("Invalid choice. Please select 1-4.")