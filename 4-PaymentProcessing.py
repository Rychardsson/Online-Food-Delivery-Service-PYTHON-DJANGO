class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        raise NotImplementedError("Subclasses must implement this method")


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, expiration_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self):
        print(f"Processing credit card payment of ${self.amount}")


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")


class BitcoinPayment(Payment):
    def __init__(self, amount, bitcoin_address):
        super().__init__(amount)
        self.bitcoin_address = bitcoin_address

    def process_payment(self):
        print(f"Processing Bitcoin payment of ${self.amount}")


credit_card_payment = CreditCardPayment(amount=100, card_number="12345-564578-901452-345546", expiration_date="12/24", cvv="123")
paypal_payment = PayPalPayment(amount=50, email="")
bitcoin_payment = BitcoinPayment(amount=75, bitcoin_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

credit_card_payment.process_payment()
paypal_payment.process_payment()
bitcoin_payment.process_payment()
