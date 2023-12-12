class DeliveryOptions:
    def __init__(self):
        self.delivery_time = None
        self.special_instructions = ""

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def set_special_instructions(self, special_instructions):
        self.special_instructions = special_instructions

    def get_delivery_time(self):
        return self.delivery_time

    def get_special_instructions(self):
        return self.special_instructions


if __name__ == "__main__":
    delivery_options = DeliveryOptions()

    delivery_options.set_delivery_time("2:00 PM")

    delivery_options.set_special_instructions("Ring the doorbell twice.")

    print("Delivery Time:", delivery_options.get_delivery_time())
    print("Special Instructions:", delivery_options.get_special_instructions())
