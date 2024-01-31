import json
import uuid

class Order:
    def __init__(self, restaurant, items):
        self.restaurant = restaurant
        self.items = items
        self.status = "Pending"
        self.total_price = sum(item['price'] for item in items)
        self.delivery_status = "Preparing"
        self.payment_status = "Not Paid"
        self.order_id = generate_order_id()

    def apply_discount(self, promotions):
        for promotion_name, discount in promotions.promotions.items():
            self.discount += discount
        discounted_price = self.total_price * (1 - self.discount)
        return discounted_price

    def update_delivery_status(self, new_status):
        self.delivery_status = new_status

    def process_payment(self):
        if self.payment_status == "Not Paid":
            self.payment_status = "Paid"
            return True
        return False

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = Menu(self)
        self.prices = Prices(self)
        self.promotions = Promotions(self)
        self.orders = []
        self.order_history = []
        self.delivery_options = []  # Lista para opções de entrega personalizáveis
        self.customer_support = CustomerSupport()  # Interface de suporte ao cliente
        self.save_to_json()

    def update_profile(self, name, location):
        self.name = name
        self.location = location
        self.save_to_json()

    def display_profile(self):
        profile = f"Restaurant: {self.name}, Location: {self.location}"
        menu_info = self.menu.display_menu()
        prices_info = self.prices.display_prices()
        return f"{profile}\n{menu_info}\n{prices_info}"

    def save_to_json(self):
        restaurant_data = {
            "name": self.name,
            "location": self.location,
            "menu": [item.__dict__ for item in self.menu.items],
            "prices": self.prices.prices
        }
        with open('restaurant_data.json', 'w') as file:
            json.dump(restaurant_data, file, indent=4)

    def place_order(self, items):
        order = Order(self, items)
        payment_successful = order.process_payment()
        if payment_successful:
            self.orders.append(order)
            self.save_to_json()
            return order
        else:
            print("Payment failed. Order not placed.")
            return None

    def display_orders(self):
        order_info = "Orders:"
        for order in self.orders:
            order_info += f"\n- {order}"
        return order_info

    def track_delivery(self, order):
        if order in self.orders:
            return order.delivery_status
        else:
            return "Order not found"

    def add_to_order_history(self, order):
        self.order_history.append(order)

    def display_order_history(self):
        order_history_info = "Order History:"
        for order in self.order_history:
            order_history_info += f"\n- Order ID: {order.order_id}, Status: {order.status}"
        return order_history_info

    def add_delivery_option(self, delivery_option):
        self.delivery_options.append(delivery_option)

    def customize_delivery_options(self, options):     
        for option in options:
            option_exists = False
            for existing_option in self.delivery_options:
                if existing_option['name'] == option['name']:
                    option_exists = True
                    break

            if not option_exists:
                self.delivery_options.append(option)
                print(f"Delivery option '{option['name']}' added.")
            else:
                print(f"Delivery option '{option['name']}' already exists and was not added.")

        self.save_to_json()

    def display_delivery_options(self):
        options_info = "Delivery Options:"
        for option in self.delivery_options:
            options_info += f"\n- {option}"
        return options_info

class Menu:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        menu_info = "Menu:"
        for item in self.items:
            menu_info += f"\n- {item['name']}: {item['description']} - ${item['price']:.2f}"
        return menu_info

class Prices:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.prices = {}

    def set_price(self, item_name, price):
        self.prices[item_name] = price

    def display_prices(self):
        prices_info = "Prices:"
        for item_name, price in self.prices.items():
            prices_info += f"\n- {item_name}: ${price:.2f}"
        return prices_info

class Promotions:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.promotions = {}

    def add_promotion(self, promotion_name, discount):
        self.promotions[promotion_name] = discount

    def remove_promotion(self, promotion_name):
        if promotion_name in self.promotions:
            del self.promotions[promotion_name]

    def display_promotions(self):
        promotions_info = "Promotions and Discounts:"
        for promotion_name, discount in self.promotions.items():
            promotions_info += f"\n- {promotion_name}: {discount * 100}% off"
        return promotions_info

class CustomerSupport:
    def __init__(self):
        self.inquiries = []

    def add_inquiry(self, inquiry):
        self.inquiries.append(inquiry)

    def display_inquiries(self):
        inquiries_info = "Customer Inquiries:"
        for inquiry in self.inquiries:
            inquiries_info += f"\n- {inquiry}"
        return inquiries_info
    
def generate_order_id():
    #a biblioteca UUID para gerar um ID único universal
    return str(uuid.uuid4())

def main():
    restaurant_name = input("Enter the restaurant name: ")
    restaurant_location = input("Enter the restaurant location: ")

    my_restaurant = Restaurant(restaurant_name, restaurant_location)

    while True:
        item_name = input("Enter the menu item name (or 'exit' to quit): ")
        if item_name.lower() == 'exit':
            break

        item_description = input("Enter the menu item description: ")
        item_price = float(input("Enter the menu item price: "))

        menu_item = {
            "name": item_name,
            "description": item_description,
            "price": item_price
        }

        my_restaurant.menu.add_item(menu_item)

    while True:
        display_options = input("Enter 'orders' to display current orders, 'track' to track an order, "
                                "'history' to view order history, 'delivery' to customize delivery options, "
                                "'support' to access customer support, or 'exit' to quit: ")
        if display_options.lower() == 'exit':
            break
        elif display_options.lower() == 'orders':
            print(my_restaurant.display_orders())
        elif display_options.lower() == 'track':
            order_id = input("Enter the order ID to track: ")
            order_to_track = None
            for order in my_restaurant.orders:
                if str(order.order_id) == order_id:
                    order_to_track = order
                    break
            if order_to_track:
                delivery_status = my_restaurant.track_delivery(order_to_track)
                print(f"Delivery Status: {delivery_status}")
            else:
                print("Order not found")
        elif display_options.lower() == 'history':
            print(my_restaurant.display_order_history())
        elif display_options.lower() == 'delivery':
            delivery_option = input("Enter a customizable delivery option: ")
            my_restaurant.customize_delivery_options([{'name': delivery_option}])
            print("Delivery option added.")
        elif display_options.lower() == 'support':
            inquiry = input("Enter your customer inquiry: ")
            my_restaurant.customer_support.add_inquiry(inquiry)
            print("Inquiry submitted.")
    
    while True:
        item_name = input("Enter the menu item name (or 'exit' to quit): ")
        if item_name.lower() == 'exit':
            break

    while True:
        promotion_option = input("Enter 'add' to add a promotion, 'remove' to remove a promotion, 'promotions' to display promotions, or 'exit' to quit: ")
        if promotion_option.lower() == 'exit':
            break
        elif promotion_option.lower() == 'add':
            promotion_name = input("Enter the promotion name: ")
            discount = float(input("Enter the discount (in decimal, e.g., 0.10 for 10%): "))
            my_restaurant.promotions.add_promotion(promotion_name, discount)
            print("Promotion added.")
        elif promotion_option.lower() == 'remove':
            promotion_name = input("Enter the promotion name to remove: ")
            my_restaurant.promotions.remove_promotion(promotion_name)
            print("Promotion removed.")
        elif promotion_option.lower() == 'promotions':
            print(my_restaurant.promotions.display_promotions())
    
    print(my_restaurant.display_profile())

if __name__ == "__main__":
    main()
