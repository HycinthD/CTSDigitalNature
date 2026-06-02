import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

    def is_over_budget(self):
        return self.spent > self.limit


categories = {
    "Food": Category("Food", 5000),
    "Travel": Category("Travel", 3000),
    "Entertainment": Category("Entertainment", 3000)
}

while True:
    category = input("Enter category (Food/Travel/Entertainment) or 'done': ")

    if category.lower() == "done":
        break

    if category not in categories:
        print("Invalid category")
        continue

    try:
        amount = float(input("Enter expense amount: "))
        categories[category].add_expense(amount)

        if categories[category].is_over_budget():
            print(f"Alert: {category} budget exceeded!")

    except ValueError:
        print("Invalid amount")

print("\nMonthly Budget Summary")
print("-" * 30)

labels = []
amounts = []

for category in categories.values():
    print(
        f"{category.name}: "
        f"Spent ₹{category.spent:.2f} / "
        f"Limit ₹{category.limit:.2f}"
    )

    labels.append(category.name)
    amounts.append(category.spent)

plt.pie(
    amounts,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Monthly Spending Distribution")
plt.show()