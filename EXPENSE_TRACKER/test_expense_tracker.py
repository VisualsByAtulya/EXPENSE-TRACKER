"""A small test file for checking the storage functions."""


import tempfile
import unittest
from pathlib import Path

import storage


class ExpenseTrackerTest(unittest.TestCase):

    def test_save_and_load(self):
        # Use a temporary file so the real expenses.json is not changed by the test.
        old_file = storage.DATA_FILE

        with tempfile.TemporaryDirectory() as folder:
            storage.DATA_FILE = Path(folder) / "test.json"

            data = {
                "expenses": [
                    {
                        "id": 1,
                        "date": "2026-09-30",
                        "amount": 100.0,
                        "category": "Food",
                        "note": "Lunch"
                    }
                ],
                "budget": 5000.0
            }

            storage.save_data(data)
            result = storage.load_data()

            self.assertEqual(result["budget"], 5000.0)
            self.assertEqual(len(result["expenses"]), 1)

        # Put the original file path back after the test finishes.
        storage.DATA_FILE = old_file


if __name__ == "__main__":
    unittest.main()
