def expense_tracker():
    expenses = []
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show All Expenses & Total")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            item = input("What did you buy? ")
            try:
                price = float(input(f"How much did the {item} cost? "))
                expenses.append({"item": item, "price": price})
                print("Added!")
            except ValueError:
                print("Invalid price. Please enter a number.")

        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nYour Expenses:")
                total = 0
                for exp in expenses:
                    print(f"- {exp['item']}: ${exp['price']:.2f}")
                    total += exp['price']
                print(f"--- Total Spent: ${total:.2f} ---")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    expense_tracker()