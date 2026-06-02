class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Perishable(Product):
    pass

class Electronics(Product):
    pass

inventory = {
    "Milk": Perishable("Milk", 5),
    "Bread": Perishable("Bread", 2),
    "Laptop": Electronics("Laptop", 10),
    "Mouse": Electronics("Mouse", 3)
}

low_stock = set()

for product in inventory.values():
    if product.stock < 5:
        low_stock.add(product.name)

print("Inventory Summary")
print("-" * 30)

for product in inventory.values():
    print(f"{product.name}: {product.stock} units")

print("\nLow Stock Alerts")
for item in low_stock:
    print(item)