class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.extend([item] * quantity)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def generate_report(self):
        print(f"Restaurant: {self.name}")
        print("Orders:")
        for i, order in enumerate(self.orders, 1):
            total = order.calculate_total()
            print(f"Order {i}: Customer {order.customer.name}, Total: ${total}")

if __name__ == "__main__":
    my_restaurant = Restaurant("My Restaurant")

    burger = MenuItem("Burger", 10.99)
    pizza = MenuItem("Pizza", 12.99)
    salad = MenuItem("Salad", 7.99)

    my_restaurant.menu.add_item(burger)
    my_restaurant.menu.add_item(pizza)
    my_restaurant.menu.add_item(salad)

    alice = Customer("Alice")
    ryc = Customer("ryc")

    order1 = Order(alice)
    order1.add_item(burger, quantity=2)
    order1.add_item(pizza)

    order2 = Order(ryc)
    order2.add_item(salad, quantity=3)

    my_restaurant.add_order(order1)
    my_restaurant.add_order(order2)

    my_restaurant.generate_report()
