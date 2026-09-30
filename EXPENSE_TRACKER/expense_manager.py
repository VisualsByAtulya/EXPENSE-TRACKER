"""Main class that handles the expense data."""


from expense import Expense
from storage import load_data, save_data


class ExpenseManager:
    def __init__(self):
        self.data = load_data()

    def add_expense(self, date, amount, category, note):
        expenses = self.data["expenses"]

        # Give the first expense ID 1, then keep increasing the largest ID.
        if len(expenses) == 0:
            new_id = 1
        else:
            new_id = max(item["id"] for item in expenses) + 1

        expense = Expense(new_id, date, amount, category, note)
        expenses.append(expense.to_dict())
        save_data(self.data)

    def get_all_expenses(self):
        # Showing older dates first makes the list easier to read.
        return sorted(
            self.data["expenses"],
            key=lambda item: item["date"]
        )

    def delete_expense(self, expense_id):
        old_count = len(self.data["expenses"])

        self.data["expenses"] = [
            item for item in self.data["expenses"]
            if item["id"] != expense_id
        ]

        if len(self.data["expenses"]) < old_count:
            save_data(self.data)
            return True

        return False

    def set_budget(self, amount):
        self.data["budget"] = amount
        save_data(self.data)

    def get_budget(self):
        return self.data.get("budget", 0)

    def total_expenses(self):
        total = 0

        for item in self.data["expenses"]:
            total += item["amount"]

        return total
