from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

        @abstractmethod
        def apply_promotion(self,product, quantity):
            pass

class PercentageDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = product.discount * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return full_price_items * product.price + half_price_items * (product.price / 2)

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        chargeable_items = quantity - (quantity // 3)
        return chargeable_items * product.price
