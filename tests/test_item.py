"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from utils import FILE_TEST_CSV


def test_calculate_total_price(test_product):
    assert test_product.calculate_total_price() == 2000.0


def test_apply_discount(test_product):
    assert test_product.price == 100.00
    test_product.pay_rate = 0.5
    test_product.apply_discount()
    assert test_product.price == 50.0


def test_instantiate_from_csv():
    """
    Тесты класс метода, через тестовый файл csv в пакете tests
    """
    Item.instantiate_from_csv(FILE_TEST_CSV)
    assert len(Item.all) == 6
    item1 = Item.all[5]
    assert int(item1.quantity) == 10


def test_string_to_number():
    """
    Тесты статического метода
    """
    assert Item.string_to_number("10.25") == 10
    assert Item.string_to_number("0") == 0
    assert Item.string_to_number("-7") == -7


def test__repr__():
    item_repr = Item("Смартфон", 10000, 20)
    assert isinstance(item_repr.__repr__(), str)
    assert len(item_repr.__repr__()) == 27


def test__str__():
    item_str = Item("Клавиатура", 75, 5)
    assert len(item_str.__str__()) == 10
    assert item_str.__str__() == "Клавиатура"
    assert isinstance(item_str.__str__(), str)
