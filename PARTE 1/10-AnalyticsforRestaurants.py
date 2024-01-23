import sqlite3

class Analytics:
    def __init__(self):
        self.conn = sqlite3.connect('restaurant_data.db')
        self.cursor = self.conn.cursor()

    def get_total_orders(self):
        self.cursor.execute('SELECT COUNT(*) FROM orders')
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_total_customers(self):
        self.cursor.execute('SELECT COUNT(*) FROM customers')
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_popular_dishes(self, top_n=5):
        self.cursor.execute('SELECT products FROM orders')
        results = self.cursor.fetchall()
        all_products = [product for result in results for product in result[0].split(', ')]
        dish_counts = {dish: all_products.count(dish) for dish in set(all_products)}
        sorted_dishes = sorted(dish_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_dishes[:top_n]

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    analytics = Analytics()

    total_orders = analytics.get_total_orders()
    print(f"Total Orders: {total_orders}")

    total_customers = analytics.get_total_customers()
    print(f"Total Customers: {total_customers}")

    popular_dishes = analytics.get_popular_dishes()
    print("Popular Dishes:")
    for dish, count in popular_dishes:
        print(f"- {dish}: {count} orders")

    analytics.close_connection()
