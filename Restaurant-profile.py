class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = Menu()

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class ItemMenu:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class menu:
  def ___init__(self, ):


class itemMenu:
  def __init__(self, valor):
    self.valor


my_restaurant = Restaurant("Restaurante ", "Localização")

# Criando itens do menu
item1 = ItemMenu("Prato1", "Descrição do Prato 1", 15.99)
item2 = ItemMenu("Prato2", "Descrição do Prato 2", 12.50)

# Adicionando itens ao menu do restaurante
my_restaurant.menu.add_item(item1)
my_restaurant.menu.add_item(item2)

#informações do restaurante e do menu
print(f"Restaurante: {my_restaurant.name}, {my_restaurant.location}")
print("Menu:")
for item in my_restaurant.menu.items:
    print(f"- {item.name}: {item.description} - ${item.price:.2f}")