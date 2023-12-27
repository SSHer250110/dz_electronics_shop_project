"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from utils import FILE_TEST_CSV, EXC_FILE_TEST_CSV


def test_calculate_total_price(test_product):
    """
    Тест метода рассчитывающего общую стоимость конкретного товара в магазине.
    """
    assert test_product.calculate_total_price() == 2000.0


def test_apply_discount(test_product):
    """
    Тест метода применяющего установленную скидку для конкретного товара.
    """
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


def test_instantiate_from_csv_exception():
    """
    Тест исключения InstantiateCSVError
    """
    with pytest.raises(InstantiateCSVError, match="InstantiateCSVError: Файл item.csv поврежден"):
        Item.instantiate_from_csv(EXC_FILE_TEST_CSV)


def test_string_to_number():
    """
    Тесты статического метода
    """
    assert Item.string_to_number("10.25") == 10
    assert Item.string_to_number("0") == 0
    assert Item.string_to_number("-7") == -7


def test__repr__():
    """
    Тест метода отображающего информацию в режиме отладки.
    """
    item_repr = Item("Смартфон", 10000, 20)
    assert isinstance(item_repr.__repr__(), str)
    assert len(item_repr.__repr__()) == 27


def test__str__():
    """
    Тест метода отображающего информацию для пользователя.
    """
    item_str = Item("Клавиатура", 75, 5)
    assert len(item_str.__str__()) == 10
    assert item_str.__str__() == "Клавиатура"
    assert isinstance(item_str.__str__(), str)


def test___add__():
    """
    Тест метода по сложению экземпляров классов
    """
    phone1 = Phone("iPhone 14", 120_000, 10, 2)
    item1 = Item("Кабель", 5000, 20)
    assert item1 + phone1 == 30
    assert phone1 + phone1 == 20
