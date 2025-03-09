import csv

EXPENSES_FILE = "expenses.csv"

# Global variable for selected currency
CURRENCY = "₹"  # Default currency is Rupees

def select_currency():
    global CURRENCY
    print("\nCurrency Options:")
    print("1 - ₹ (Rupees)")
    print("2 - $ (US Dollars)")
    print("3 - € (Euros)")
    
    choice = input("Enter the number for your currency choice: ")
    if choice == "1":
        CURRENCY = "₹"
    elif choice == "2":
        CURRENCY = "$"
    elif choice == "3":
        CURRENCY = "€"
    else:
        print("Invalid choice. Defaulting to ₹ (Rupees).")
        CURRENCY = "₹"
    print(f"Currency switched to {CURRENCY}.")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input(f"Enter amount ({CURRENCY}): "))
    
    with open(EXPENSES_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("Expense added successfully!")

def view_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            reader = csv.reader(file)
            print(f"\nDate        | Category  | Amount ({CURRENCY})")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {CURRENCY}{float(row[2]):,.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def generate_report():
    category_totals = {}
    
    try:
        with open(EXPENSES_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                category_totals[category] = category_totals.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
    
    print(f"\nExpense Report ({CURRENCY}):")
    for category, total in category_totals.items():
        print(f"{category}: {CURRENCY}{total:,.2f}")

def main():
    print("Welcome to the Expense Tracker!")
    select_currency()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Switch Currency")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            select_currency()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()