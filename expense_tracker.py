# Personal Expense Tracker
# First Python Project

expenses = []

# Function to add a new expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Function to display all expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses available.")
    else:
        print("\nYour Expenses:")

        for expense in expenses:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("--------------------")


# Function to calculate total expenses
def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses:", total)


# Main program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")