import time
from datetime import datetime

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

class Promotion:
    def __init__(self, name, description, start_date, end_date, restaurant_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.restaurant_id = restaurant_id

    def is_valid(self, current_date):
        return self.start_date <= current_date <= self.end_date

class Discount:
    def __init__(self, name, amount, discount_type, restaurant_id):
        self.name = name
        self.amount = amount
        self.discount_type = discount_type  # 'percentage' or 'fixed'
        self.restaurant_id = restaurant_id

    def apply_discount(self, original_price):
        if self.discount_type == 'percentage':
            return original_price * (1 - self.amount / 100)
        elif self.discount_type == 'fixed':
            return original_price - self.amount
        else:
            raise ValueError("Invalid discount type")

class Restaurant:
    def __init__(self, name, location, cuisine):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.menu = Menu()
        self.prices = Prices()
        self.promotions = []
        self.discounts = []
        self.orders = []

    def manage_profile(self):
        print(f"Managing profile for restaurant {self.name}")

    def manage_menu(self):
        print(f"Managing menu for restaurant {self.name}")

    def manage_pricing(self):
        print(f"Managing pricing for restaurant {self.name}")

    def manage_promotions(self):
        print(f"Managing promotions for restaurant {self.name}")

    def manage_discounts(self):
        print(f"Managing discounts for restaurant {self.name}")

    def view_order_history(self, user):
        user_orders = [order for order in self.orders if order.customer_name == user.username]
        print(f"Order history for restaurant {self.name} and user {user.username}:")
        for order in user_orders:
            print(f"- Order ID: {order.order_id}, Status: {order.status}")

    def get_valid_promotions(self, current_date):
        return [promotion for promotion in self.promotions if promotion.is_valid(current_date)]

    def apply_discount(self, original_price, discount_name):
        for discount in self.discounts:
            if discount.name == discount_name:
                return discount.apply_discount(original_price)
        return original_price

class UserProfile:
    def __init__(self, username):
        self.username = username
        self.orders = []

    def place_order(self, restaurant, items, delivery_options):
        order_id = len(self.orders) + 1
        new_order = Order(order_id, restaurant, self.username, items, delivery_options)
        self.orders.append(new_order)
        restaurant.orders.append(new_order)  # Adiciona o pedido ao histórico do restaurante
        print(f"Order placed successfully by {self.username}")
        return new_order

    def track_orders(self):
        if not self.orders:
            print("No orders to track.")
        else:
            print(f"Orders for {self.username}:")
            for order in self.orders:
                print(f"- Order ID: {order.order_id}, Status: {order.status}, Restaurant: {order.restaurant.name}")

class Order:
    def __init__(self, order_id, restaurant, customer_name, items, delivery_options):
        self.order_id = order_id
        self.restaurant = restaurant
        self.customer_name = customer_name
        self.items = items
        self.status = "Pending"
        self.delivery_options = delivery_options
        self.payment = None

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to {new_status}")

    def add_payment(self, payment):
        self.payment = payment
        print(f"Payment of ${payment.amount} processed for Order {self.order_id}")

class Payment:
    def __init__(self, amount, order_id, payment_method):
        self.amount = amount
        self.order_id = order_id
        self.payment_method = payment_method

    def process_payment(self):
        print(f"Processing {self.payment_method} payment of ${self.amount}")

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

    def customize_options(self):
        print("Customizing delivery options")

class CustomerSupport:
    @staticmethod
    def handle_inquiry(order_id):
        print(f"Handling inquiry for Order {order_id}")

class Analytics:
    def get_total_orders(self):
        return len(Order.orders)

    def get_total_customers(self):
        return len(set(order.customer_name for order in Order.orders))

    def get_popular_dishes(self, top_n=5):
        all_products = [product for order in Order.orders for product in order.items]
        dish_counts = {dish: all_products.count(dish) for dish in set(all_products)}
        sorted_dishes = sorted(dish_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_dishes[:top_n]

def print_menu():
    print("\n------ Restaurant Management System ------")
    print("1. Manage Restaurant Profile")
    print("2. Manage Menu")
    print("3. Manage Pricing")
    print("4. Manage Promotions")
    print("5. Manage Discounts")
    print("6. View Order History")
    print("7. Place Order")
    print("8. Track Orders")
    print("9. Customer Support")
    print("10. Analytics")
    print("exit. Exit")

def main_menu(restaurant, user_profile, analytics):
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            restaurant.manage_profile()
        elif choice == '2':
            restaurant.manage_menu()
        elif choice == '3':
            restaurant.manage_pricing()
        elif choice == '4':
            restaurant.manage_promotions()
        elif choice == '5':
            restaurant.manage_discounts()
        elif choice == '6':
            restaurant.view_order_history(user_profile)
        elif choice == '7':
            place_order_menu(restaurant, user_profile)
        elif choice == '8':
            user_profile.track_orders()
        elif choice == '9':
            CustomerSupport.handle_inquiry(order_id=input("Enter Order ID for inquiry: "))
        elif choice == '10':
            display_analytics(analytics)
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")

def place_order_menu(restaurant, user_profile):
    print("\n------ Place Order ------")
    print(restaurant.menu.display_menu())

    items = []
    while True:
        item_name = input("Enter item name to add to the order (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break

        item = restaurant.menu.get_item_by_name(item_name)
        if item:
            items.append(item)
            print(f"{item_name} added to the order.")
        else:
            print(f"Item '{item_name}' not found in the menu.")

    delivery_options = customize_delivery_options()

    user_profile.place_order(restaurant, items, delivery_options)

def customize_delivery_options():
    print("\n------ Customize Delivery Options ------")
    delivery_options = DeliveryOptions()

    delivery_time = input("Enter desired delivery time: ")
    delivery_options.set_delivery_time(delivery_time)

    special_instructions = input("Enter special instructions for delivery: ")
    delivery_options.set_special_instructions(special_instructions)

    print("Delivery options customized successfully.")
    return delivery_options

def display_analytics(analytics):
    print("\n------ Analytics ------")
    total_orders = analytics.get_total_orders()
    print(f"Total Orders: {total_orders}")

    total_customers = analytics.get_total_customers()
    print(f"Total Customers: {total_customers}")

    popular_dishes = analytics.get_popular_dishes()
    print("Popular Dishes:")
    for dish, count in popular_dishes:
        print(f"- {dish}: {count} orders")

def initialize_system():
    print("\n------ Welcome to the Restaurant Management System ------")
    restaurant_name = input("Enter the restaurant name: ")
    restaurant_location = input("Enter the restaurant location: ")
    restaurant_cuisine = input("Enter the restaurant cuisine: ")

    my_restaurant = Restaurant(name=restaurant_name, location=restaurant_location, cuisine=restaurant_cuisine)

    item_name = input("Enter the menu item name: ")
    item_description = input("Enter the menu item description: ")
    item_price = float(input("Enter the menu item price: "))
    menu_item = MenuItem(name=item_name, description=item_description, price=item_price)
    my_restaurant.menu.add_item(menu_item)

    print(my_restaurant.prices.display_prices())
    print(my_restaurant.menu.display_menu())

    promotion_name = input("Enter the promotion name: ")
    promotion_description = input("Enter the promotion description: ")
    start_date = input("Enter the promotion start date (YYYY-MM-DD): ")
    end_date = input("Enter the promotion end date (YYYY-MM-DD): ")
    promotion = Promotion(name=promotion_name, description=promotion_description, start_date=start_date, end_date=end_date, restaurant_id=None)
    my_restaurant.promotions.append(promotion)

    discount_name = input("Enter the discount name: ")
    discount_amount = float(input("Enter the discount amount: "))
    discount_type = input("Enter the discount type (percentage/fixed): ")
    discount = Discount(name=discount_name, amount=discount_amount, discount_type=discount_type, restaurant_id=None)
    my_restaurant.discounts.append(discount)

    user_name = input("Enter your username: ")
    user_profile = UserProfile(username=user_name)

    print(my_restaurant.menu.display_menu())
    selected_item = input("Enter the item you want to order: ")
    selected_item = my_restaurant.menu.get_item_by_name(selected_item)

    if selected_item:
        items = [selected_item]
        delivery_options = customize_delivery_options()
        user_profile.place_order(my_restaurant, items, delivery_options)
    else:
        print("Invalid item. Order placement failed.")

    return my_restaurant, user_profile, Analytics()

if __name__ == "__main__":
    restaurant, user_profile, analytics = initialize_system()

    try:
        main_menu(restaurant, user_profile, analytics)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("Exiting the Restaurant Management System. Goodbye!")