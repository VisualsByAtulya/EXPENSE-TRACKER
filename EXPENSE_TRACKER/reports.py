"""Functions used to display different expense reports."""


from collections import defaultdict
from utils import line, money


def show_monthly_report(manager):
    month = input("Enter month (YYYY-MM): ").strip()

    # Only expenses whose date starts with the entered month are selected.
    expenses = [
        item for item in manager.get_all_expenses()
        if item["date"].startswith(month)
    ]

    print("\nMONTHLY REPORT")
    print(line())

    if len(expenses) == 0:
        print("No expenses found for this month.")
        return

    total = 0

    for item in expenses:
        total += item["amount"]

    print("Month:", month)
    print("Number of expenses:", len(expenses))
    print("Total spent:", money(total))

    budget = manager.get_budget()

    if budget > 0:
        print("Monthly budget:", money(budget))
        print("Remaining:", money(budget - total))


def show_category_report(manager):
    print("\nCATEGORY REPORT")
    print(line())

    categories = defaultdict(float)

    # Add the amount to the correct category.
    for item in manager.get_all_expenses():
        categories[item["category"]] += item["amount"]

    if len(categories) == 0:
        print("No expenses found.")
        return

    for category, amount in sorted(categories.items()):
        print(f"{category:<18} {money(amount)}")
