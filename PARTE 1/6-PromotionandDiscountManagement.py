import sqlite3
import time

class Promotion:
    def __init__(self, name, description, start_date, end_date, restaurant_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.restaurant_id = restaurant_id

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO promotions (name, description, start_date, end_date, restaurant_id) VALUES (?, ?, ?, ?, ?)',
                       (self.name, self.description, self.start_date, self.end_date, self.restaurant_id))
        conn.commit()
        conn.close()

    def is_valid(self, current_date):
        return self.start_date <= current_date <= self.end_date


class Discount:
    def __init__(self, name, amount, discount_type, restaurant_id):
        self.name = name
        self.amount = amount
        self.discount_type = discount_type  # 'percentage' or 'fixed'
        self.restaurant_id = restaurant_id

    def save_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO discounts (name, amount, discount_type, restaurant_id) VALUES (?, ?, ?, ?)',
                       (self.name, self.amount, self.discount_type, self.restaurant_id))
        conn.commit()
        conn.close()

    def apply_discount(self, original_price):
        if self.discount_type == 'percentage':
            return original_price * (1 - self.amount / 100)
        elif self.discount_type == 'fixed':
            return original_price - self.amount
        else:
            raise ValueError("Invalid discount type")


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.promotions = []
        self.discounts = []

    def add_promotion(self, promotion):
        promotion.save_to_db()
        self.promotions.append(promotion)

    def add_discount(self, discount):
        discount.save_to_db()
        self.discounts.append(discount)

    def get_valid_promotions(self, current_date):
        return [promotion for promotion in self.promotions if promotion.is_valid(current_date)]

    def apply_discount(self, original_price, discount_name):
        for discount in self.discounts:
            if discount.name == discount_name:
                return discount.apply_discount(original_price)
        return original_price


if __name__ == "__main__":
    restaurant_name = input("Enter the restaurant name: ")
    my_restaurant = Restaurant(restaurant_name)

    promotion1 = Promotion("Summer Special", "Get 20% off on selected items", "2023-06-01", "2023-08-31", restaurant_id=None)
    my_restaurant.add_promotion(promotion1)

    discount1 = Discount("Early Bird Discount", 5, 'percentage', restaurant_id=None)
    my_restaurant.add_discount(discount1)

    current_date = "2023-07-15"
    valid_promotions = my_restaurant.get_valid_promotions(current_date)
    print(f"Valid promotions on {current_date}: {[promotion.name for promotion in valid_promotions]}")

    original_price = 100
    discount_name = "Early Bird Discount"
    discounted_price = my_restaurant.apply_discount(original_price, discount_name)
    print(f"Original Price: ${original_price}, Discounted Price: ${discounted_price}")
