from src.item import Item


class Phone(Item):
    """
    Класс описывающий товар телефон
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param quantity: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        """
        Метод для отображения информации в режиме отладки.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Метод для отображения информации для пользователя.
        """
        return self.name

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Метод с условиями, присваивающий новое значение атрибуту
        """
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
