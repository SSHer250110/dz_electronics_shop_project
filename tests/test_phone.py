import pytest

from src.phone import Phone


def test__repr__():
    """
    Тест метода отображающего информацию в режиме отладки.
    """
    phone_repr = Phone("Samsung S22", 10000, 20, 3)
    assert isinstance(phone_repr.__repr__(), str)


def test__str__():
    """
    Тест метода отображающего информацию для пользователя.
    """
    phone_str = Phone("iPhone 15 Pro", 75, 5, 1)
    assert phone_str.__str__() == "iPhone 15 Pro"
    assert isinstance(phone_str.__str__(), str)


def test_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 5)
    assert phone.number_of_sim == 5
    assert isinstance(phone.number_of_sim, int)
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
