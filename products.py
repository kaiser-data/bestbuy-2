class Product:
    """
    Represents a product with a name, price, and quantity. Also handles promotions.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity available.

        Raises:
            ValueError: If the name is empty or price/quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError('Name cannot be empty, and price or quantity cannot be negative')

        self._name = name
        self._price = float(price)
        self._quantity = int(quantity)
        self.active = True
        self.promotion = None

    @property
    def name(self) -> str:
        """Returns the name of the product."""
        return self._name

    @property
    def price(self) -> float:
        """Gets the price of the product."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Sets the price of the product with validation."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self) -> int:
        """Gets the quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """Sets the quantity of the product and deactivates if zero."""
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activates the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self.active = False

    def buy(self, purchase_quantity: int) -> float:
        """Processes a purchase, reducing quantity and calculating cost."""
        if purchase_quantity <= 0:
            raise ValueError('Quantity to buy must be greater than zero')
        if self._quantity >= purchase_quantity:
            self._quantity -= purchase_quantity
            if self.promotion:
                return self.promotion.apply_promotion(self, purchase_quantity)
            return self._price * purchase_quantity
        else:
            raise ValueError('Not enough quantity in stock')

    def set_promotion(self, promotion) -> None:
        """Sets a promotion for the product."""
        self.promotion = promotion

    def __str__(self) -> str:
        """Returns a string representation of the product."""
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self._name}, Price: ${self._price:,.2f}, Quantity: {self._quantity}{promotion_info}"

    def __gt__(self, other: "Product") -> bool:
        """Compares product prices for greater-than comparison."""
        if isinstance(other, Product):
            return self._price > other._price
        return NotImplemented

    def __lt__(self, other: "Product") -> bool:
        """Compares product prices for less-than comparison."""
        if isinstance(other, Product):
            return self._price < other._price
        return NotImplemented


class NonStockedProduct(Product):
    """Represents a product that is not stocked and has unlimited availability."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def buy(self, purchase_quantity: int) -> float:
        """Allows purchasing without reducing stock."""
        if purchase_quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero")
        if self.promotion:
            return self.promotion.apply_promotion(self, purchase_quantity)
        return self.price * purchase_quantity

    def __str__(self) -> str:
        """Returns a string representation of the non-stocked product with promotion info."""
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price:,.2f}, Non-stocked Item{promotion_info}"


class LimitedProduct(Product):
    """Represents a product with a purchase limit per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, purchase_quantity: int) -> float:
        """Allows purchasing within the defined limit."""
        if purchase_quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} units of {self.name} per transaction.")
        return super().buy(purchase_quantity)

    def __str__(self) -> str:
        """Returns a string representation of the limited product."""
        return f"{self.name}, Price: ${self.price:,.2f}, Limited Item (Max {self.maximum} per order)"