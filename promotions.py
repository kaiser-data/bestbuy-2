from abc import ABC, abstractmethod
from products import Product, NonStockedProduct, LimitedProduct


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        """Initializes a promotion with a name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Applies the promotion to a product purchase."""
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount to the product price."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Calculates the price after applying the percentage discount."""
        discount = product.price * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """Applies a promotion where the second product is half-price."""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Calculates the total price using the second-half price promotion."""
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return full_price_items * product.price + half_price_items * (product.price / 2)


class ThirdOneFree(Promotion):
    """Applies a promotion where every third product is free."""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Calculates the total price using the third-one-free promotion."""
        chargeable_items = quantity - (quantity // 3)
        return chargeable_items * product.price


if __name__ == '__main__':

    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     Product("Google Pixel 7", price=500, quantity=250),
                     NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                   ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Test products and promotions
    for product in product_list:
        print(str(product))

    # Simulate buying with promotions
    print("\nPurchase Scenarios:")
    print(f"Buying 2 MacBook Air M2: ${product_list[0].buy(2)}")
    print(f"Buying 3 Bose QuietComfort Earbuds: ${product_list[1].buy(3)}")
    print(f"Buying 1 Windows License: ${product_list[3].buy(1)}")
