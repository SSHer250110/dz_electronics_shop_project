"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(test_product):
    assert test_product.calculate_total_price() == 2000.0


def test_apply_discount(test_product):
    assert test_product.price == 100.00
    test_product.pay_rate = 0.5
    test_product.apply_discount()
    assert test_product.price == 50.0
