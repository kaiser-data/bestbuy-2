import pytest
from products import Product, NonStockedProduct, LimitedProduct
from store import Store

# Setup initial stock of inventory
@pytest.fixture
def inventory():
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)
    best_buy = Store([mac, bose])
    return mac, bose, pixel, best_buy

# Test product price validation
def test_invalid_price():
    with pytest.raises(ValueError, match=".*negative.*"):
        Product("Invalid Product", price=-100, quantity=10)

# Test string representation
def test_product_str(inventory):
    mac, _, _, _ = inventory
    assert str(mac) == "MacBook Air M2, Price: $1,450.00, Quantity: 100"

# Test price comparison
def test_price_comparison(inventory):
    mac, bose, _, _ = inventory
    assert mac > bose

# Test product existence in store
def test_product_in_store(inventory):
    mac, _, pixel, best_buy = inventory
    assert mac in best_buy
    assert pixel not in best_buy

# Test store length
def test_store_length(inventory):
    _, _, _, best_buy = inventory
    assert len(best_buy) == 2

# Test store product retrieval
def test_store_indexing(inventory):
    mac, _, _, best_buy = inventory
    assert best_buy[0] == mac

# Test store merging
def test_store_addition(inventory):
    mac, bose, pixel, best_buy = inventory
    second_store = Store([pixel])
    merged_store = best_buy + second_store
    assert len(merged_store) == 3
    assert pixel in merged_store

# Fixture for a valid product
@pytest.fixture
def valid_product():
    return Product(name="MacBook Air M2", price=1450, quantity=100)

# Test valid product creation
def test_create_normal_product(valid_product):
    assert valid_product.name == "MacBook Air M2"
    assert valid_product.price == 1450
    assert valid_product.quantity == 100
    assert valid_product.is_active() is True

# Parameterized tests for invalid products
@pytest.mark.parametrize("name, price, quantity", [
    ("", 1450, 100),
    ("MacBook Air M2", -1450, 100),
    ("MacBook Air M2", 1450, -1),
])
def test_create_invalid_product(name, price, quantity):
    with pytest.raises(ValueError):
        Product(name=name, price=price, quantity=quantity)

# Test product deactivation
def test_product_becomes_inactive_when_quantity_zero(valid_product):
    valid_product.quantity = 0
    assert valid_product.is_active() is False

# Test product purchase
def test_buy_reduces_quantity_and_returns_total_price(valid_product):
    purchase_quantity = 3
    total_price = valid_product.buy(purchase_quantity)
    assert valid_product.quantity == 97
    assert total_price == 4350

# Test insufficient stock purchase
def test_buy_larger_quantity_than_stock_raises_exception(valid_product):
    purchase_quantity = valid_product.quantity + 1
    with pytest.raises(ValueError, match="Not enough quantity in stock"):
        valid_product.buy(purchase_quantity)

# Test making an order with promotions
def test_make_order_with_promotions(inventory):
    mac, bose, _, best_buy = inventory
    shopping_list = [(mac, 2), (bose, 3)]
    total_payment, total_savings = best_buy.order(shopping_list)
    assert total_payment > 0
    assert total_savings >= 0
    assert mac.quantity == 98
    assert bose.quantity == 497
