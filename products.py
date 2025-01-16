class Product:
    """
    A class to represent a product with attributes for name, price, quantity, and active status.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product. Must be non-negative.
        quantity (int): The quantity of the product in stock. Must be non-negative.
        active (bool): Whether the product is active or not. Defaults to True.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product with the given name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity of the product in stock. Must be non-negative.

        Raises:
            ValueError: If the name is empty or if price or quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError('Name cannot be empty, and price or quantity cannot be negative')

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def get_quantity(self) -> float:
        """
        Get the current quantity of the product.

        Returns:
            int: The quantity of the product in stock.
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Set the quantity of the product and deactivate it if the quantity becomes zero.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        Check if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active == True

    def activate(self) -> None:
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Gets a string representation of the product.

        Returns:
            str: A string containing the product's name, price, and quantity.
        """
        return f"{self.name}, Price: ${self.price:,.2f}, Quantity: {self.quantity}"

    def buy(self, purchase_quantity) -> float:
        """
        Buy a specified quantity of the product.

        Args:
            purchase_quantity (int): The quantity to purchase. Must be greater than zero.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If purchase_quantity is not greater than zero or if there is insufficient stock.
        """
        if purchase_quantity <= 0:
            raise ValueError('Quantity to buy must be greater than zero')
        if self.quantity >= purchase_quantity:
            self.quantity -= purchase_quantity
            return self.price * purchase_quantity
        else:
            raise ValueError('Not enough quantity in stock')

