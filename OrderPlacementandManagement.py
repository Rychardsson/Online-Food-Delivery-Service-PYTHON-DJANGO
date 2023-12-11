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


