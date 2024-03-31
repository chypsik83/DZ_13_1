import pytest

from src.class_product import Category, Product


@pytest.fixture
def test_category():
    return Category("Яблоко", "Фрукты", [])


def test_init(test_category):
    assert test_category.name == "Яблоко"
    assert test_category.description == "Фрукты"
    assert test_category.total_categories == 1
    assert test_category.counter_product == 0


@pytest.fixture
def test_product():
    return Product('Яблоко', "Фрукты", 20.1, 20)


def test_init_product(test_product):
    assert test_product.name == 'Яблоко'
    assert test_product.description == "Фрукты"
    assert test_product.price == 20.1
    assert test_product.quantity == 20


def test_counter_product(test_category):
    assert test_category.counter_product == 0
