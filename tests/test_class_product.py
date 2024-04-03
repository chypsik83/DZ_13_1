import pytest

from src.class_product import Category, Product


@pytest.fixture
def products():
    return [Product("Яблоко", "Россия", 10.99, 100),
            Product("Банан", "Импорт", 20.50, 50)]


@pytest.fixture
def category(products):
    Category("Фрукты", "Производитель", products)


def test__init(category, products):
    assert category.name == "Фрукты"
    assert category.description == "Производитель"
    assert category.products == products


def test_product(category, products):
    assert Category.counter_product == 2


def test_category(category, products):
    assert Category.total_categories == 1


@pytest.fixture
def product():
    return Product("Яблоко", "Россия", 10.99, 100)


def test_product_init(product):
    assert product.name == "Яблоко"
    assert product.description == "Россия"
    assert product.price == 10.99
    assert product.quantity == 100
