import csv
from datetime import datetime

def expense_tracker():
    try:
        current_month = datetime.now().month
        current_year = datetime.now().year

        category_totals = {}

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            current_month_expenses = [
                row for row in reader
                if datetime.strptime(
                    row["date"], "%Y-%m-%d"
                ).month == current_month
                and datetime.strptime(
                    row["date"], "%Y-%m-%d"
                ).year == current_year
            ]

        for expense in current_month_expenses:
            category = expense["category"]
            amount = float(expense["amount"])

            category_totals[category] = (
                category_totals.get(category, 0) + amount
            )

        print("Expense Summary")

        for category, total in category_totals.items():
            print(f"{category}: {total:.2f}")

    except FileNotFoundError:
        print("expenses.csv not found")

expense_tracker()