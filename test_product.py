import pytest
from products import Product


# Fixture for a valid product
@pytest.fixture
def valid_product():
    return Product(name="MacBook Air M2", price=1450, quantity=100)


def test_create_normal_product(valid_product):
    """
    Test that a valid product is created successfully.
    """
    assert valid_product.name == "MacBook Air M2"
    assert valid_product.price == 1450
    assert valid_product.quantity == 100
    assert valid_product.is_active() is True


# Test creating a product with invalid details using parametrized tests
@pytest.mark.parametrize("name, price, quantity", [
    ("", 1450, 100),
    ("MacBook Air M2", -1450, 100),
    ("MacBook Air M2", 1450, -1),
])
def test_create_invalid_product(name, price, quantity):
    """
    This parameterized test ensures that invalid inputs for the Product class raise a ValueError.

    Edge cases tested include:
    - Empty name
    - Negative price
    - Negative quantity
      """
    with pytest.raises(ValueError):
        Product(name=name, price=price, quantity=quantity)


def test_product_becomes_inactive_when_quantity_zero(valid_product):
    """
    Test that a product becomes inactive after its entire quantity is purchased.
    """
    valid_product.set_quantity(quantity=0)
    assert valid_product.is_active() is False


def test_buy_reduces_quantity_and_returns_total_price(valid_product):
    """
    Test that the `buy` method reduces quantity and returns the correct total price.
    """
    purchase_quantity = 3
    total_price = valid_product.buy(purchase_quantity)

    assert valid_product.quantity == 97
    assert total_price == 4350


def test_buy_larger_quantity_than_stock_raises_exception(valid_product):
    """
    Test that attempting to buy more than available stock raises a ValueError.
    """
    purchase_quantity = valid_product.quantity + 1

    with pytest.raises(ValueError, match="Not enough quantity in stock"):
        valid_product.buy(purchase_quantity)


