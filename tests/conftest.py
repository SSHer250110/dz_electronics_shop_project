import pytest

from src.item import Item


@pytest.fixture
def test_product():
    return Item("product", 100.0, 20)
