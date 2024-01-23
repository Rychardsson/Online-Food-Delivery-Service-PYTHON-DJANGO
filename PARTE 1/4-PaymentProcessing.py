import sqlite3

class Payment:
    def __init__(self, amount, order_id):
        self.amount = amount
        self.order_id = order_id

    def process_payment(self):
        raise NotImplementedError("Subclasses must implement this method")

    def save_payment_to_db(self, payment_type):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO payments (order_id, amount, payment_type) VALUES (?, ?, ?)',
                       (self.order_id, self.amount, payment_type))
        conn.commit()
        conn.close()

class CreditCardPayment(Payment):
    def __init__(self, amount, order_id, card_number, expiration_date, cvv):
        super().__init__(amount, order_id)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self):
        print(f"Processing credit card payment of ${self.amount}")
        self.save_payment_to_db("Credit Card")

class PayPalPayment(Payment):
    def __init__(self, amount, order_id, email):
        super().__init__(amount, order_id)
        self.email = email

    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")
        self.save_payment_to_db("PayPal")

class BitcoinPayment(Payment):
    def __init__(self, amount, order_id, bitcoin_address):
        super().__init__(amount, order_id)
        self.bitcoin_address = bitcoin_address

    def process_payment(self):
        print(f"Processing Bitcoin payment of ${self.amount}")
        self.save_payment_to_db("Bitcoin")

order_id = int(input("Enter the order ID: "))
payment_amount = float(input("Enter the payment amount: "))

credit_card_payment = CreditCardPayment(amount=payment_amount, order_id=order_id, card_number="12345-564578-901452-345546", expiration_date="12/24", cvv="123")

paypal_payment = PayPalPayment(amount=payment_amount, order_id=order_id, email="rgs@ic.ufal.br")

bitcoin_payment = BitcoinPayment(amount=payment_amount, order_id=order_id, bitcoin_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

credit_card_payment.process_payment()
paypal_payment.process_payment()
bitcoin_payment.process_payment()
