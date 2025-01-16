"""
This module defines the functionality of the store class using product class to manage products for the main.py
"""

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


    def add_product(self, product):
        """
        Adds a Product object to the store.

        Args:
            product (Product): The Product object to be added.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a Product object from the store.

        Args:
            product (Product): The Product object to be removed.
        """
        self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Calculates and returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """
        return sum(product.quantity for product in self.product_list)

    def get_all_products(self):
        """
         Retrieves all active products in the store.

         Returns:
             List[Product]: A list of active Product objects.
         """
        return [product for product in self.product_list if product.is_active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order and calculates the total price.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains
                a Product object and the quantity to order.

        Returns:
            float: The total price of the order.

        Raises:
            ValueError: If a product is not available in the store.
        """
        total_price = 0.0
        active_products = self.get_all_products()

        for product, quantity in shopping_list:
            if product in active_products:
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available in the store.")

        return total_price



