import pytest


class Category:
    name = str
    description = str
    product = list
    total_categories = 0
    counter_product = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.products = product

        Category.total_categories += 1
        Category.counter_product += len(product)


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


