from src.item import Item


class MixinKeyboard:
    """
    Класс-миксин, дополнительная функциональность для класса,
    описывающего товар клавиатура
    """

    def __init__(self):
        """
        Создание экземпляра класса язык раскладки
        """
        self._language = "EN"

    def change_lang(self):
        """
        Метод переключения языка клавиатуры с условиями
        """
        if self._language == "EN" or self._language == "RU":
            if self._language == "EN":
                self._language = "RU"
            else:
                self._language = "EN"
            return self._language
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
        self._language = "EN"

    def __str__(self):
        """
        Метод для отображения информации для пользователя.
        """
        if self.name:
            return self.name
        else:
            return self._language

    @property
    def language(self):
        return self._language
