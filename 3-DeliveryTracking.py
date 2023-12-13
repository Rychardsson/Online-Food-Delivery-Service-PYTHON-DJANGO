import time
import sqlite3

class Delivery:
    def __init__(self, delivery_id, status="Pending"):
        self.delivery_id = delivery_id
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

class DeliveryTracker:
    def __init__(self):
        self.deliveries = {}

    def add_delivery(self, delivery_id, order_id):
        if delivery_id not in self.deliveries:
            self.deliveries[delivery_id] = Delivery(delivery_id)
            self.save_delivery_to_db(delivery_id, order_id)
        else:
            print(f"Delivery {delivery_id} already exists.")

    def update_delivery_status(self, delivery_id, new_status):
        if delivery_id in self.deliveries:
            self.deliveries[delivery_id].update_status(new_status)
            self.update_delivery_in_db(delivery_id, new_status)
        else:
            print(f"Delivery {delivery_id} does not exist.")

    def get_delivery_status(self, delivery_id):
        if delivery_id in self.deliveries:
            return self.deliveries[delivery_id].status
        else:
            return f"Delivery {delivery_id} does not exist."

    def save_delivery_to_db(self, delivery_id, order_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO deliveries (delivery_id, order_id, status) VALUES (?, ?, ?)',
                       (delivery_id, order_id, "Pending"))
        conn.commit()
        conn.close()

    def update_delivery_in_db(self, delivery_id, new_status):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE deliveries SET status=? WHERE delivery_id=?',
                       (new_status, delivery_id))
        conn.commit()
        conn.close()

def simulate_delivery_tracking(tracker):
    for delivery_id in tracker.deliveries:
        tracker.update_delivery_status(delivery_id, "In Progress")
        time.sleep(2)
        tracker.update_delivery_status(delivery_id, "Delivered")
        time.sleep(2)

if __name__ == "__main__":
    tracker = DeliveryTracker()

    conn = sqlite3.connect('restaurant_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT order_id FROM orders')
    orders = cursor.fetchall()
    conn.close()

    for order_id in orders:
        tracker.add_delivery(order_id[0], order_id[0])

    simulate_delivery_tracking(tracker)

    for delivery_id in tracker.deliveries:
        status = tracker.get_delivery_status(delivery_id)
        print(f"Delivery {delivery_id}: {status}")
