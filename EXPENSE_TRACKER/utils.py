"""Some small helper functions used in the project."""


def line():
    # Used to print the separator line in the menu and reports.
    return "-" * 40


def money(amount):
    # Keeping the money format in one place makes the output easier to manage.
    return "Rs. " + format(amount, ".2f")
