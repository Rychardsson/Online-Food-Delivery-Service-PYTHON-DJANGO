import json

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = Menu()
        self.prices = Prices()

    def update_profile(self, name, location):
        self.name = name
        self.location = location

    def display_profile(self):
        profile = f"Restaurant: {self.name}, Location: {self.location}"
        menu_info = self.menu.display_menu()
        prices_info = self.prices.display_prices()
        return f"{profile}\n{menu_info}\n{prices_info}"

    def save_to_json(self, file_name):
        data = {
            "name": self.name,
            "location": self.location,
            "menu": [item.__dict__ for item in self.menu.items],
            "prices": self.prices.prices
        }

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=2)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)

        self.name = data["name"]
        self.location = data["location"]

        self.menu.items = [MenuItem(**item) for item in data["menu"]]
        self.prices.prices = data["prices"]


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

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


class Prices:
    def __init__(self):
        self.prices = {}

    def set_price(self, item_name, price):
        self.prices[item_name] = price

    def display_prices(self):
        prices_info = "Prices:"
        for item_name, price in self.prices.items():
            prices_info += f"\n- {item_name}: ${price:.2f}"
        return prices_info


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

json_file_name = input("Enter the JSON file name to save: ")
my_restaurant.save_to_json(json_file_name)

json_file_to_load = input("Enter the JSON file name to load: ")
my_restaurant.load_from_json(json_file_to_load)

print(my_restaurant.display_profile())
