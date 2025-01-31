from typing import List, Tuple
from products import Product

class Store:
    """
    A class to represent a store that manages products.

    Attributes:
        product_list (List[Product]): A list of Product objects available in the store.
    """

    def __init__(self, product_list: List[Product]):
        """
        Initializes the Store instance with a list of products.

        Args:
            product_list (List[Product]): The initial list of products to be managed by the store.
        """
        self.product_list = product_list

    def add_product(self, product: Product) -> None:
        """Adds a Product object to the store."""
        self.product_list.append(product)

    def remove_product(self, product: Product) -> None:
        """Removes a Product object from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Calculates and returns the total quantity of all products in the store."""
        return sum(product.quantity for product in self.product_list)

    def get_all_products(self) -> List[Product]:
        """Retrieves all active products in the store."""
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> Tuple[float, float]:
        """
        Processes an order and calculates the total price and total savings.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains
                a Product object and the quantity to order.

        Returns:
            Tuple[float, float]: The total price of the order and total savings from promotions.

        Raises:
            ValueError: If a product is not available in the store.
        """
        total_price = 0.0
        total_savings = 0.0
        active_products = self.get_all_products()

        for product, quantity in shopping_list:
            if product in active_products:
                original_price = product.price * quantity
                final_price = product.buy(quantity)
                savings = original_price - final_price
                total_price += final_price
                total_savings += savings
            else:
                raise ValueError(f"Product {product.name} is not available in the store.")

        return total_price, total_savings

    def __contains__(self, product: Product) -> bool:
        """Checks if a product exists in the store."""
        return product in self.product_list

    def __add__(self, other: "Store") -> "Store":
        """Merges two stores and returns a new Store instance."""
        if isinstance(other, Store):
            return Store(self.product_list + other.product_list)
        return NotImplemented

    def __len__(self) -> int:
        """Returns the total number of unique products in the store."""
        return len(self.product_list)

    def __str__(self) -> str:
        """Returns a string representation of the store with numbered products."""
        product_details = "\n".join(f"{index}. {product}" for index, product in enumerate(self.product_list, start=1))
        return f"Store Inventory:\n{product_details}"

    # Add __getitem__ to Store class
    def __getitem__(self, index):
        """Allows indexing to access products in the store."""
        return self.product_list[index]