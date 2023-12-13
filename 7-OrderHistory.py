import sqlite3

class Order:
    def __init__(self, order_id, user_id, items, total_price):
        self.order_id = order_id
        self.user_id = user_id
        self.items = items
        self.total_price = total_price

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(f"  - {item}")
        print(f"Total Price: ${self.total_price:.2f}")
        print("------------------------")

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (order_id, user_id, total_price) VALUES (?, ?, ?)',
                       (self.order_id, self.user_id, self.total_price))
        for item in self.items:
            cursor.execute('INSERT INTO order_items (order_id, item) VALUES (?, ?)',
                           (self.order_id, item))
        conn.commit()
        conn.close()

    def load_from_db(cls, order_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT user_id, total_price FROM orders WHERE order_id=?', (order_id,))
        result = cursor.fetchone()
        if result:
            user_id, total_price = result
            cursor.execute('SELECT item FROM order_items WHERE order_id=?', (order_id,))
            items = [item[0] for item in cursor.fetchall()]
            conn.close()
            return cls(order_id, user_id, items, total_price)
        else:
            conn.close()
            return None

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []

    def place_order(self, items, total_price):
        order_id = len(self.orders) + 1
        new_order = Order(order_id, self.user_id, items, total_price)
        new_order.save_to_db()
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

    def load_orders_by_user_id(cls, user_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT order_id FROM orders WHERE user_id=?', (user_id,))
        order_ids = [order[0] for order in cursor.fetchall()]
        conn.close()
        return [Order.load_from_db(order_id) for order_id in order_ids]

if __name__ == "__main__":
    user_id = 1
    user1 = User(user_id, "rychardsson")

    user1.place_order(["Item1", "Item2", "Item3"], 50.00)
    user1.place_order(["Item4", "Item5"], 30.00)

    user1.view_order_history()

    user1.reorder_favorite(1)
