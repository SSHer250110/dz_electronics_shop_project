from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Employee и дочерние')

    # @property
    # def number_of_sim(self):
    #     return self.number_of_sim
    #
    # @number_of_sim.setter
    # def number_of_sim(self, number_of_sim):
    #     if number_of_sim > 0 and number_of_sim is int:
    #         self.number_of_sim = number_of_sim
    #     raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
