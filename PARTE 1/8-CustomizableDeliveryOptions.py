import sqlite3

class DeliveryOptions:
    def __init__(self, delivery_time=None, special_instructions=""):
        self.delivery_time = delivery_time
        self.special_instructions = special_instructions

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def set_special_instructions(self, special_instructions):
        self.special_instructions = special_instructions

    def get_delivery_time(self):
        return self.delivery_time

    def get_special_instructions(self):
        return self.special_instructions

    def save_to_db(self, order_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO delivery_options (order_id, delivery_time, special_instructions) VALUES (?, ?, ?)',
                       (order_id, self.delivery_time, self.special_instructions))
        conn.commit()
        conn.close()

    def load_from_db(cls, order_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT delivery_time, special_instructions FROM delivery_options WHERE order_id=?', (order_id,))
        result = cursor.fetchone()
        conn.close()
        return cls(*result) if result else None

if __name__ == "__main__":
    order_id = 1
    delivery_options = DeliveryOptions()

    delivery_options.set_delivery_time("2:00 PM")
    delivery_options.set_special_instructions("Ring the doorbell twice.")

    delivery_options.save_to_db(order_id)

    loaded_delivery_options = DeliveryOptions.load_from_db(order_id)

    print("Delivery Time:", loaded_delivery_options.get_delivery_time())
    print("Special Instructions:", loaded_delivery_options.get_special_instructions())
