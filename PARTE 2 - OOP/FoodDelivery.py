import sqlite3

class DatabaseManager:
    @staticmethod
    def create_tables():
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                restaurant_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                restaurant_id INTEGER NOT NULL,
                item_name TEXT NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                order_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        conn.commit()
        conn.close()

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = Menu()
        self.prices = Prices()

        self.save_to_db()

    def update_profile(self, name, location):
        self.name = name
        self.location = location
        self.update_db_profile()

    def display_profile(self):
        profile = f"Restaurant: {self.name}, Location: {self.location}"
        menu_info = self.menu.display_menu()
        prices_info = self.prices.display_prices()
        return f"{profile}\n{menu_info}\n{prices_info}"

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO restaurants (name, location) VALUES (?, ?)', (self.name, self.location))
        conn.commit()
        conn.close()

    def update_db_profile(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE restaurants SET name=?, location=? WHERE name=? AND location=?',
                       (self.name, self.location, self.name, self.location))
        conn.commit()
        conn.close()

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        item.save_to_db()

    def display_menu(self):
        menu_info = "Menu:"
        for item in self.items:
            menu_info += f"\n- {item.name}: {item.description} - ${item.price:.2f}"
        return menu_info

class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO menu_items (restaurant_id, name, description, price) VALUES (?, ?, ?, ?)',
                       (my_restaurant.get_restaurant_id(), self.name, self.description, self.price))
        conn.commit()
        conn.close()

class Prices:
    def __init__(self):
        self.prices = {}

    def set_price(self, item_name, price):
        self.prices[item_name] = price
        self.save_price_to_db(item_name, price)

    def display_prices(self):
        prices_info = "Prices:"
        for item_name, price in self.prices.items():
            prices_info += f"\n- {item_name}: ${price:.2f}"
        return prices_info

    def save_price_to_db(self, item_name, price):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO prices (restaurant_id, item_name, price) VALUES (?, ?, ?)',
                       (my_restaurant.get_restaurant_id(), item_name, price))
        conn.commit()
        conn.close()

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

DatabaseManager.create_tables()

restaurant_name = input("Enter the restaurant name: ")
restaurant_location = input("Enter the restaurant location: ")
my_restaurant = Restaurant(restaurant_name, restaurant_location)

while True:
    item_name = input("Enter the menu item name (or 'exit' to quit): ")
    if item_name.lower() == 'exit':
        break

    item_description = input("Enter the menu item description: ")
    item_price = float(input("Enter the menu item price: "))
    menu_item = MenuItem(item_name, item_description, item_price)
    my_restaurant.menu.add_item(menu_item)

while True:
    item_name = input("Enter the item name to set the price (or 'exit' to quit): ")
    if item_name.lower() == 'exit':
        break

    item_price = float(input(f"Enter the price for {item_name}: "))
    my_restaurant.prices.set_price(item_name, item_price)

user_name = input("Enter the username: ")
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
