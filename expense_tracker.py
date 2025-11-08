# Smart Expense Tracker
from colorama import Fore, Style, init
init(autoreset=True)
import csv
import os

FILENAME = 'expenses.csv'

# Step 1: Check if file exists; if not, create one with headers
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item', 'Amount', 'Category'])

# Step 2: Function to display all expenses
def show_expenses():
    print(Fore.CYAN + "\n------ Expense Tracker ------")
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
        total = 0
        for expense in expenses:
            print(Fore.YELLOW + f"Item: {expense['Item']}, Amount: ₹{expense['Amount']}, Category: {expense['Category']}")
            total += int(expense['Amount'])
        print(Fore.CYAN + "\n---------------------------------")
        print(Fore.GREEN + f"Total Monthly Expense: ₹{total}")
        print(Fore.CYAN + "---------------------------------\n")

# Step 3: Function to add a new expense
def add_expense():
    item = input(Fore.BLUE + "Enter expense item: ")
    amount = input(Fore.BLUE + "Enter amount (₹): ")
    category = input(Fore.BLUE + "Enter category: ")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item, amount, category])
    
    print(Fore.GREEN + f"✅ Added: {item} - ₹{amount} ({category})\n")

# Step 4: Main menu
while True:
    print(Fore.MAGENTA + "1️⃣  View Expenses")
    print(Fore.MAGENTA + "2️⃣  Add New Expense")
    print(Fore.MAGENTA + "3️⃣  Exit")
    choice = input(Fore.CYAN + "Choose an option (1/2/3): ")

    if choice == '1':
        show_expenses()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        print(Fore.RED + "👋 Exiting... Thank you for using Smart Expense Tracker!")
        break
    else:
        print(Fore.RED + "❌ Invalid choice! Try again.\n")
