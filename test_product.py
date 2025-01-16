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