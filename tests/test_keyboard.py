import pytest

from src.keyboard import Keyboard


def test_change_lang():
    """
    Тест метода переключения языка клавиатуры с условиями
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    with pytest.raises(AttributeError):
        kb.language = "DE"


def test__str__():
    """
    Тест метода отображающего информацию для пользователя.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.name) == "Dark Project KD87A"
    assert isinstance(kb.__str__(), str)
    assert str(kb.language) == "EN"
