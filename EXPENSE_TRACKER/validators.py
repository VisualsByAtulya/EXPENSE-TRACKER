"""Functions that check the values entered by the user."""


from datetime import datetime


CATEGORIES = [
    "Food",
    "Rent",
    "Books",
    "Transport",
    "Fees",
    "Entertainment",
    "Health",
    "Shopping",
    "Other"
]


def get_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please use YYYY-MM-DD, for example 2026-09-30.")


def get_amount(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return round(value, 2)

            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a number.")


def get_category():
    print("\nCategories:")

    # enumerate gives us the number to show beside each category.
    for number, category in enumerate(CATEGORIES, start=1):
        print(number, "-", category)

    while True:
        try:
            choice = int(input("Choose a category number: "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Please choose a number from the list.")
        except ValueError:
            print("Please enter a number.")


def get_text(message):
    value = input(message).strip()

    if value == "":
        return "No note"

    return value
