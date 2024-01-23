import sqlite3

class Review:
    def __init__(self, customer_name, rating, comment, dish_id):
        self.customer_name = customer_name
        self.rating = rating
        self.comment = comment
        self.dish_id = dish_id

    def save_review_to_db(self):
        conn = sqlite3.connect('restaurant_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO reviews (customer_name, rating, comment, dish_id) VALUES (?, ?, ?, ?)',
                       (self.customer_name, self.rating, self.comment, self.dish_id))
        conn.commit()
        conn.close()

class Dish:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        review.save_review_to_db()

    def average_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def get_dish_by_name(self, dish_name):
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        return None

restaurant_name = input("Enter the restaurant name: ")
restaurant_cuisine = input("Enter the restaurant cuisine: ")

my_restaurant = Restaurant(name=restaurant_name, cuisine=restaurant_cuisine)

while True:
    dish_name = input("Enter the dish name (or 'exit' to quit): ")
    if dish_name.lower() == 'exit':
        break

    dish_description = input("Enter the dish description: ")
    dish = Dish(name=dish_name, description=dish_description)

    review_customer_name = input("Enter your name for the review: ")
    review_rating = int(input("Enter the rating for the dish (1-5): "))
    review_comment = input("Enter your comment: ")

    review = Review(customer_name=review_customer_name, rating=review_rating, comment=review_comment, dish_id=None)
    dish.add_review(review)

    my_restaurant.add_dish(dish)

dish_to_find = input("Enter the dish name to find: ")
found_dish = my_restaurant.get_dish_by_name(dish_to_find)
if found_dish:
    print(f"The average rating for {dish_to_find} is: {found_dish.average_rating()}")
else:
    print(f"Dish '{dish_to_find}' not found.")
