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


