class Order:
    def __init__(self, order_id, items, total_price):
        self.order_id = order_id
        self.items = items
        self.total_price = total_price

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(f"  - {item}")
        print(f"Total Price: ${self.total_price:.2f}")
        print("------------------------")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []

    def place_order(self, items, total_price):
        order_id = len(self.orders) + 1
        new_order = Order(order_id, items, total_price)
        self.orders.append(new_order)
        print(f"Order placed successfully! Order ID: {order_id}")

    def view_order_history(self):
        if not self.orders:
            print("No order history available.")
        else:
            print(f"Order History for {self.name}:")
            for order in self.orders:
                order.display_order()

    def reorder_favorite(self, order_id):
        if 1 <= order_id <= len(self.orders):
            order_to_reorder = self.orders[order_id - 1]
            print(f"Reordering items from Order ID {order_id}:")
            order_to_reorder.display_order()
        else:
            print("Invalid order ID. Please enter a valid order ID.")


user1 = User(1, "rychardsson")
user1.place_order(["Item1", "Item2", "Item3"], 50.00)
user1.place_order(["Item4", "Item5"], 30.00)

user1.view_order_history()

user1.reorder_favorite(1)
