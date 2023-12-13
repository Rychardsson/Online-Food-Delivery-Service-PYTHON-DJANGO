import sqlite3

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        order.save_to_db(self.user_id)
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

    def save_to_db(self, user_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (user_id, order_id, status) VALUES (?, ?, ?)',
                       (user_id, self.order_id, self.status))
        conn.commit()

user_name = input("Enter the username: ")
user_location = input("Enter the user location: ")

my_user = User(user_id=1, username=user_name)

while True:
    order_id = int(input("Enter the order ID (or 0 to exit): "))
    if order_id == 0:
        break

    order_items = input("Enter the order items (comma-separated): ").split(',')
    order = Order(order_id, order_items)
    my_user.place_order(order)

for order in my_user.orders:
    new_status = input(f"Enter the new status for order {order.order_id}: ")
    order.update_status(new_status)

my_user.track_orders()
