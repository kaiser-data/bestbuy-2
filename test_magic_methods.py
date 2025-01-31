import pytest
from products import Product, LimitedProduct
from store import Store

# Setup fixture for inventory
@pytest.fixture
def inventory():
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)
    best_buy = Store([mac, bose, pixel])
    return mac, bose, pixel, best_buy

# Test store properties and magic methods
def test_store_properties(inventory):
    mac, bose, pixel, best_buy = inventory

    # Test negative price assignment
    with pytest.raises(ValueError):
        mac.price = -100

    # Test string representation
    assert str(mac) == "MacBook Air M2, Price: $1,450.00, Quantity: 100"

    # Test price comparison
    assert mac > bose

    # Test product existence in store
    assert mac in best_buy
    assert pixel in best_buy