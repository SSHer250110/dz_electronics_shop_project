import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("ware", 1000.0, 20)
