"""
Expense Tracker
A small beginner-friendly project for the VITyarthi Build Your Own Project.

Run:
    python main.py
"""

from expense_manager import ExpenseManager
from reports import show_monthly_report, show_category_report
from validators import get_amount, get_date, get_category, get_text
from utils import line, money


def add_expense(manager):
    print("\nADD EXPENSE")
    print(line())

    date = get_date("Enter date (YYYY-MM-DD): ")
    amount = get_amount("Enter amount: ")
    category = get_category()
    note = get_text("Enter a short note: ")

    manager.add_expense(date, amount, category, note)
    print("\nExpense saved successfully.")


def view_expenses(manager):
    print("\nALL EXPENSES")
    print(line())

    expenses = manager.get_all_expenses()

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("ID  Date        Category        Amount       Note")
    print("-" * 58)

    for expense in expenses:
        # The spacing here keeps the table looking like a simple terminal table.
        print(
            f"{expense['id']:<3} "
            f"{expense['date']:<11} "
            f"{expense['category']:<15} "
            f"{money(expense['amount']):>10}   "
            f"{expense['note']}"
        )

    print("-" * 58)
    print("Total:", money(manager.total_expenses()))


def delete_expense(manager):
    print("\nDELETE EXPENSE")
    print(line())

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Please enter a number.")
        return

    if manager.delete_expense(expense_id):
        print("Expense deleted.")
    else:
        print("Expense ID not found.")


def set_budget(manager):
    print("\nMONTHLY BUDGET")
    print(line())

    amount = get_amount("Enter monthly budget: ")
    manager.set_budget(amount)
    print("Budget saved.")


def show_budget(manager):
    print("\nBUDGET STATUS")
    print(line())

    budget = manager.get_budget()
    spent = manager.total_expenses()

    if budget == 0:
        print("Budget is not set.")
        return

    remaining = budget - spent

    print("Budget :", money(budget))
    print("Spent  :", money(spent))
    print("Left   :", money(remaining))

    if remaining < 0:
        print("You are over the budget by", money(abs(remaining)))
    else:
        print("You still have", money(remaining), "left.")


def menu():
    print("\n" + "=" * 40)
    print("        STUDENT EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Monthly report")
    print("4. Category report")
    print("5. Delete expense")
    print("6. Set monthly budget")
    print("7. View budget status")
    print("0. Exit")
    print("=" * 40)


def main():
    manager = ExpenseManager()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)
        elif choice == "2":
            view_expenses(manager)
        elif choice == "3":
            show_monthly_report(manager)
        elif choice == "4":
            show_category_report(manager)
        elif choice == "5":
            delete_expense(manager)
        elif choice == "6":
            set_budget(manager)
        elif choice == "7":
            show_budget(manager)
        elif choice == "0":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
