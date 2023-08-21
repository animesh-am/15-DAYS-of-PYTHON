import json


class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = max(0, price)  # Ensure non-negative values
        self.__quantity = max(0, quantity)

    def __str__(self):
        return f"Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"


# Load products from JSON file and create Product objects
with open('five.json', 'r') as file:
    products = [Product(item["name"], item["price"], item["quantity"]) for item in json.load(file)]

# Display products
for product in products:
    print(product)
