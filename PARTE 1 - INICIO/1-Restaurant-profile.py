import sqlite3

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
                       (self.get_restaurant_id(), self.name, self.description, self.price))
        conn.commit()
        conn.close()

    def get_restaurant_id(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM restaurants WHERE name=? AND location=?',
                       (my_restaurant.name, my_restaurant.location))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

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

Restaurant.create_tables()

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

print(my_restaurant.display_profile())
