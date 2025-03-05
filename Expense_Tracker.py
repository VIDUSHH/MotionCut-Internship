import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Ensure the file exists and has a header row
if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Add a new expense entry."""
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        
        # Validate category (should contain only letters)
        while True:
            category = input("Enter expense category (Food, Transport, Entertainment, etc.): ").strip()
            if category.isalpha():
                break
            print("\nInvalid category! Please enter a valid category (letters only).\n")

        # Validate amount (should be a positive number)
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    print("\nAmount should be a positive number.\n")
                    continue
                break
            except ValueError:
                print("\nInvalid amount! Please enter a numeric value.\n")

        description = input("Enter a brief description: ").strip()

        # Store expense in CSV file
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        
        print("\nExpense added successfully!\n")
    except Exception as e:
        print(f"\nError adding expense: {e}\n")

def view_expenses():
    """Display all recorded expenses."""
    try:
        if os.stat(FILE_NAME).st_size == 0:
            print("\nNo expenses recorded yet.\n")
            return

        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) <= 1:
                print("\nNo expenses recorded yet.\n")
                return

            print("\nRecorded Expenses:")
            for row in data:
                print("\t".join(row))
            print()
    except FileNotFoundError:
        print("\nError: The expense file does not exist!\n")
    except Exception as e:
        print(f"\nError reading expenses: {e}\n")

def monthly_summary():
    """Display a summary of expenses for the current month."""
    try:
        if os.stat(FILE_NAME).st_size == 0:
            print("\nNo expenses recorded yet.\n")
            return

        current_month = datetime.now().strftime("%Y-%m")
        expenses = {}

        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for row in reader:
                if len(row) < 3:  
                    continue
                
                date, category, amount, _ = row
                if date.startswith(current_month):
                    try:
                        amount = float(amount)
                        expenses[category] = expenses.get(category, 0) + amount
                    except ValueError:
                        continue  

        if not expenses:
            print("\nNo expenses recorded for this month.\n")
            return

        print("\nMonthly Expense Summary:")
        for category, total in expenses.items():
            print(f"{category}: ₹{total:.2f}")
        print()
    except FileNotFoundError:
        print("\nError: The expense file does not exist!\n")
    except Exception as e:
        print(f"\nError generating summary: {e}\n")

def main():
    """Main menu for user interaction."""
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("\nExiting the Expense Tracker. Have a great day!\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
