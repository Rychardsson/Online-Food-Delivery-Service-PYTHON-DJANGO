class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order placed successfully by {self.username}")

    def track_orders(self):
        if not self.orders:
            print("No orders to track.")
        else:
            print(f"Orders for {self.username}:")
            for order in self.orders:
                print(f"- Order ID: {order.order_id}, Status: {order.status}")

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to {new_status}")



user1 = User(user_id=1, username="Al")
user2 = User(user_id=2, username="Bo")


order1 = Order(order_id=101, items=["Pizza", "Burger"])
order2 = Order(order_id=102, items=["Sushi", "Salad"])

user1.place_order(order1)
user2.place_order(order2)

user1.track_orders()
user2.track_orders()

order1.update_status("In Progress")
order2.update_status("Delivered")

user1.track_orders()
user2.track_orders()
