import sys

#Loads Store Class and Product Class
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


class StoreMenu:
    """
    A class to represent the menu system interacting with the Store class.

    Attributes:
        store_obj (Store): The store instance that manages inventory and operations.
    """

    def __init__(self, store_obj: "Store") -> None:
        """
        Initializes the StoreMenu with a given Store instance.

        Args:
            store_obj (Store): The store instance.
        """
        self.store_obj = store_obj

    def print_menu(self) -> None:
        """
        Displays the store menu options to the user.
        """
        menu = """
           Store Menu
           ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """
        print(menu)

    def list_all_products(self) -> None:
        """
        Lists all available products in the store along with their details.
        """
        print("------")
        print(self.store_obj)
        print("------")

    def total_amount(self) -> None:
        """Displays the total number of unique products and the total quantity of all items in the store."""
        total_unique_items = len(self.store_obj)
        total_items = sum(product.quantity for product in self.store_obj)
        print(f"Total unique products: {total_unique_items}, Total items in stock: {total_items}")

    def make_order(self) -> None:
        """
        Allows the user to create an order by selecting products and quantities.
        Handles input validation and processes the order through the store.
        """
        self.list_all_products()
        shopping_list = []
        print("When you want to finish the order, press Enter.")

        while picked_product := input("Enter the product number (or leave blank to finish): ").strip():
            if not picked_product.isdigit() or not (
                    0 <= (picked_index := int(picked_product) - 1) < len(self.store_obj)):
                print("Error: Please enter a valid product number.")
                continue

            try:
                picked_quantity = int(input("Enter the quantity: ").strip())
                if picked_quantity > 0:
                    shopping_list.append((self.store_obj[picked_index], picked_quantity))
                else:
                    print("Error: Quantity must be a positive integer.")
            except ValueError:
                print("Error: Invalid quantity. Please enter a valid number.")

        if shopping_list:
            total_payment, total_savings = self.store_obj.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total_payment:,.2f}")
            if total_savings > 0:
                print(f"Total savings from promotions: ${total_savings:,.2f}")
        else:
            print("No items were ordered.")

    def exit_store(self) -> None:
        """
        Exits the store menu system.
        """
        sys.exit()

    def menu_logic(self, user_input: str) -> None:
        """
        Executes the appropriate action based on user input.

        Args:
            user_input (str): The menu option selected by the user.
        """
        menu_options = {
            "1": lambda: self.list_all_products(),
            "2": lambda: self.total_amount(),
            "3": lambda: self.make_order(),
            "4": lambda: self.exit_store()
        }

        if user_input in menu_options:
            menu_options[user_input]()
        else:
            print("Invalid option. Please try again.")


def main() -> None:
    """
    Sets up the store and initializes the store menu for user interaction.
    """
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
    product_list[4].set_promotion(thirty_percent)


    best_buy = Store(product_list)
    store_menu = StoreMenu(best_buy)
    while True:
        store_menu.print_menu()
        user_input = input("Please choose a number: ").strip()
        store_menu.menu_logic(user_input)


if __name__ == '__main__':
    main()

