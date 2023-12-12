class Review:
    def __init__(self, customer_name, rating, comment):
        self.customer_name = customer_name
        self.rating = rating
        self.comment = comment

class Dish:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

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

if __name__ == "__main__":
    my_restaurant = Restaurant(name="My Restaurant", cuisine="Italian")

    pasta_dish = Dish(name="Pasta", description="Spaghetti with tomato sauce")

    pasta_review = Review(customer_name="rychardsson", rating=4, comment="Delicious!")
    pasta_dish.add_review(pasta_review)

    my_restaurant.add_dish(pasta_dish)

    dish_to_find = "Pasta"
    found_dish = my_restaurant.get_dish_by_name(dish_to_find)
    if found_dish:
        print(f"The average rating for {dish_to_find} is: {found_dish.average_rating()}")
    else:
        print(f"Dish '{dish_to_find}' not found.")
