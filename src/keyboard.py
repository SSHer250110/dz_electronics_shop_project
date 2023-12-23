from src.item import Item


class MixinKeyboard:
    """
    Класс-миксин, дополнительная функциональность для класса,
    описывающего товар клавиатура
    """

    __language = "EN"

    @property
    def language(self):
        """
        Обращение к методу как к приватному атрибуту
        """
        return self.__language

    def change_lang(self):
        """
        Метод переключения языка клавиатуры с условиями
        """
        if self.__language == "EN" or self.__language == "RU":
            if self.__language == "EN":
                self.__language = "RU"
            else:
                self.__language = "EN"
            return self.__language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinKeyboard):
    """
    Класс описывающий товар клавиатура.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса клавиатура.
        """
        super().__init__(name, price, quantity)

    def __str__(self):
        """
        Метод для отображения информации для пользователя.
        """
        if self.name:
            return self.name
        else:
            return self.__language
