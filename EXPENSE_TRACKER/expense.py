"""This file stores the Expense class."""


class Expense:
    def __init__(self, expense_id, date, amount, category, note):
        self.id = expense_id
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note

    def to_dict(self):
        # A dictionary is easier to save in the JSON file.
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "note": self.note
        }
