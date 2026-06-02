import math

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [i for i in self.items if i.name != name]

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def print_receipt(self):
        total = self.calculate_total()
        gst = total * 0.18
        final_total = total + gst

        print("\nReceipt")
        print("-" * 30)

        for item in self.items:
            print(
                f"{item.name} x {item.quantity} = ₹{item.price * item.quantity}"
            )

        print(f"\nSubtotal : ₹{total:.2f}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Total    : ₹{final_total:.2f}")

cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))

cart.print_receipt()