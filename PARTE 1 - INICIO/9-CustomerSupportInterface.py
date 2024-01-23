import sqlite3

class Order:
    def __init__(self, order_number, products):
        self.order_number = order_number
        self.products = products

    def __str__(self):
        return f"Order #{self.order_number}: {', '.join(self.products)}"

    def save_to_db(self, customer_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (customer_id, order_number, products) VALUES (?, ?, ?)',
                       (customer_id, self.order_number, ', '.join(self.products)))
        conn.commit()
        conn.close()

    def load_from_db(cls, customer_id):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT order_number, products FROM orders WHERE customer_id=?', (customer_id,))
        results = cursor.fetchall()
        conn.close()
        return [cls(order_number, products.split(', ')) for order_number, products in results]

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        order.save_to_db(self.get_customer_id())
        print(f"Order placed successfully: {order}")

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)',
                       (self.name, self.email, self.phone))
        conn.commit()
        conn.close()

    def get_customer_id(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM customers WHERE email=?', (self.email,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def load_from_db(cls, email):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, email, phone FROM customers WHERE email=?', (email,))
        result = cursor.fetchone()
        conn.close()
        return cls(*result) if result else None

if __name__ == "__main__":
    customer1 = Customer("rychardsson", "rych@.com", "99155-1234")
    customer2 = Customer("Gus", "gsdd@.com", "99155-5678")

    order1 = Order(1, ["Product A", "Product B"])
    order2 = Order(2, ["Product C", "Product D"])

    customer1.place_order(order1)
    customer2.place_order(order2)

    customer1.save_to_db()
    customer2.save_to_db()

    email_to_search = "rgs@ic.ufal.br"
    found_customer = Customer.load_from_db(email_to_search)
    if found_customer:
        orders = Order.load_from_db(found_customer.get_customer_id())
        print(f"Orders for {found_customer.name}:")
        for order in orders:
            print(order)
    else:
        print("Customer not found.")
