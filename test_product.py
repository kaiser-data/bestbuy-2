import pytest

from products import Product


def test_create_normal_product():
    try:
        product = Product(name="MacBook Air M2", price=999.99, quantity=50)
    except Exception as e:
        pytest.fail(f"Product creation failed with exception: {e}")

    assert product.name == "MacBook Air M2"
    assert product.price == 999.99
    assert product.quantity == 50
    assert product.is_active() is True


# Test creating a product with invalid details using parametrized tests
@pytest.mark.parametrize("name, price, quantity", [
    ("", 999.99, 50),
    ("MacBook Air M2", -999.99, 50),
    ("MacBook Air M2", 999.99, -1),
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

def test_product_becomes_inactive_when_quantity_zero():
    product = Product(name="MacBook Air M2", price=999.99, quantity=100)

    product.set_quantity(product.quantity - product.quantity)
    assert product.is_active() is False

def test_purchase_quantity_and_total_price():
    product = Product(name="MacBook Air M2", price=1000, quantity=100)
    purchase_quantity = 3
    total_price = product.buy(purchase_quantity)

    assert product.quantity == 97
    assert  total_price == 3000


def test_buy_larger_quantity_than_stock_raises_exception():
    product = Product(name="Test Product", price=100.0, quantity=5)

    with pytest.raises(ValueError, match="Not enough quantity in stock"):
        product.buy(10)


