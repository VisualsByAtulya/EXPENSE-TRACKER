# Student Expense Tracker

## Overview

This is a simple Python project made for the VITyarthi Build Your Own Project requirement.

The project helps a student keep a record of daily expenses. It can also show a monthly report, category report and budget status.

The project is intentionally kept simple so that the code is easy to understand for a beginner.

## Features

- Add a new expense
- View all expenses
- Delete an expense
- Monthly report
- Category-wise report
- Set a monthly budget
- Check budget status
- Save data in JSON
- Basic input validation
- Simple test file

## Technologies Used

- Python 3
- JSON
- CSV concepts
- Python classes
- Functions
- Lists and dictionaries
- File handling
- unittest

No external Python packages are required.

## Project Structure

```text
expense_tracker_vityarthi/
│
├── main.py
├── expense.py
├── expense_manager.py
├── storage.py
├── validators.py
├── reports.py
├── utils.py
├── test_expense_tracker.py
├── expenses.json
├── statement.md
├── README.md
└── PROJECT_REPORT.pdf
```

## How to Run

1. Install Python 3.
2. Open this folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

## How to Test

Run:

```bash
python -m unittest test_expense_tracker.py
```

## Data Storage

The program stores the expenses in `expenses.json`. The file is created automatically when an expense is saved.

## Limitations

- It is a single-user program.
- It is terminal based.
- It does not have login functionality.
- Existing expenses are deleted and added again instead of being edited.
- The reports are text based.

## Future Improvements

- Add an edit expense option.
- Add CSV export.
- Add graphs.
- Add a login system.
- Add weekly and yearly reports.
- Add a simple graphical interface.
