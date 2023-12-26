import csv

from utils import FILE_CSV


# from utils import FILE_CSV


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:11]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path=FILE_CSV):
        """
        Класс-метод для создания экземпляров из данных csv файла.
        """
        try:
            Item.all = []
            with open(path, "r", encoding="windows-1251") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["name"]
                    price = row["price"]
                    quantity = row["quantity"]
                    cls(name, price, quantity)
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(string_int):
        """
        Статический метод для преобразования строки в целое число.
        """
        return int(float(string_int))

    def __add__(self, other):
        """
        Метод по сложению экземпляров классов
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    def __repr__(self):
        """
        Метод для отображения информации в режиме отладки.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Метод для отображения информации для пользователя.
        """
        return self.__name


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "InstantiateCSVError: Файл item.csv поврежден"

    def __str__(self):
        return self.message

Item.instantiate_from_csv()
