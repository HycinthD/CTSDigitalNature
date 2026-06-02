def add_expense(expenses, amount):
    if amount <= 0:
        print("Invalid expense amount")
        return

    expenses.append(amount)
    print("Updated Expenses:", expenses)

expenses = [500, 1200, 800]
add_expense(expenses, 300)