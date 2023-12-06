class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = Menu()
        self.pricing = Pricing()

    def update_profile(self, name, location):
        self.name = name
        self.location = location

    def display_profile(self):
        print(f"Restaurant: {self.name}, Location: {self.location}")
        self.menu.display_menu()
        self.pricing.display_pricing()


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"- {item.name}: {item.description} - ${item.price:.2f}")


class ItemMenu:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Pricing:
    def __init__(self):
        self.prices = {}

    def set_price(self, item_name, price):
        self.prices[item_name] = price

    def display_pricing(self):
        print("Pricing:")
        for item_name, price in self.prices.items():
            print(f"- {item_name}: ${price:.2f}")


my_restaurant = Restaurant("Restaurante", "Localização")

item1 = ItemMenu("Prato1", "Descrição do Prato 1", 15.99)
item2 = ItemMenu("Prato2", "Descrição do Prato 2", 12.50)

my_restaurant.menu.add_item(item1)
my_restaurant.menu.add_item(item2)

my_restaurant.display_profile()

print(f"Restaurante: {my_restaurant.name}, {my_restaurant.location}")
print("Menu:")
for item in my_restaurant.menu.items:
    print(f"- {item.name}: {item.description} - ${item.price:.2f}")

