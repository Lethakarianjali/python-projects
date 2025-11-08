import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Create file with headers if not exists
def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass


# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("✅ Expense added successfully!")


# View all expenses
def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip headers
            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet!")


# View monthly summary
def monthly_summary():
    month = input("Enter month (e.g., 2025-11): ")
    total = 0
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Date'].startswith(month):
                    total += float(row['Amount'])
        print(f"\n💰 Total expenses for {month}: ₹{total}")
    except FileNotFoundError:
        print("No data found!")


# Smart suggestion
def smart_suggestion():
    category_totals = {}
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_totals[row['Category']] = category_totals.get(row['Category'], 0) + float(row['Amount'])
        if not category_totals:
            print("No data to analyze yet.")
            return
        max_cat = max(category_totals, key=category_totals.get)
        if category_totals[max_cat] > 1000:
            print(f"⚠️ You spent the most on {max_cat} (₹{category_totals[max_cat]}). Try to save more next month!")
    except FileNotFoundError:
        print("No data available yet!")


# Menu
def menu():
    initialize_file()
    while True:
        print("\n===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Smart Suggestion")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            smart_suggestion()
        elif choice == '5':
            print("Exiting... Have a great day! 💸")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
