from src.item import Item


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
