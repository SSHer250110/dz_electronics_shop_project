from src.item import Item


class MixinKeyboard:

    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        if self._language == "EN" or self._language == "RU":
            if self._language == "EN":
                self._language = "RU"
            else:
                self._language = "EN"
            return self._language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = "EN"

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self._language

    @property
    def language(self):
        return self._language
