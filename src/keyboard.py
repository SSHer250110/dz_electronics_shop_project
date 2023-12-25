from src.item import Item


class MixinKeyboard:
    """
    Класс-миксин, дополнительная функциональность для класса,
    описывающего товар клавиатура
    """

    def __init__(self):
        """
        Создание экземпляра класса MixinKeyboard.
        :param __language: Язык раскладки клавиатуры.
        """
        self.__language = "EN"

    @property
    def language(self):
        """
        Обращение к методу как к приватному атрибуту
        """
        return self.__language

    def change_lang(self):
        """
        Метод переключения языка клавиатуры.
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self.__language


class Keyboard(Item, MixinKeyboard):
    """
    Класс описывающий товар клавиатура.
    """
    pass


kb = Keyboard('Dark Project KD87A', 9600, 5)
kb.change_lang()
print(str(kb.language))
