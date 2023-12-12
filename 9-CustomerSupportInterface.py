class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order placed successfully: {order}")

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Order:
    def __init__(self, order_number, products):
        self.order_number = order_number
        self.products = products

    def __str__(self):
        return f"Order #{self.order_number}: {', '.join(self.products)}"


class CustomerSupportInterface:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer added: {customer}")

    def find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def display_customer_orders(self, customer):
        if customer:
            print(f"Orders for {customer.name}:")
            for order in customer.orders:
                print(order)
        else:
            print("Customer not found.")

if __name__ == "__main__":
    customer1 = Customer("rychardsson", "rych@.com", "99155-1234")
    customer2 = Customer("Gus", "gsdd@.com", "99155-5678")

    order1 = Order(1, ["Product A", "Product B"])
    order2 = Order(2, ["Product C", "Product D"])

    customer1.place_order(order1)
    customer2.place_order(order2)

    support_interface = CustomerSupportInterface()

    support_interface.add_customer(customer1)
    support_interface.add_customer(customer2)

    email_to_search = "rych@.com"
    found_customer = support_interface.find_customer_by_email(email_to_search)
    support_interface.display_customer_orders(found_customer)
