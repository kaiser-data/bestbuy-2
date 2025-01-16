import pytest

from products import Product


def test_create_normal_product():
    product = ProductProduct("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active is True

