"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item1():

    """ Экземпляр класса в фикстуре """

    return Item("Смартфон", 10000, 20)


def test_1(item1):

    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):

    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):

    Item.pay_rate = 0.8

    assert item1.apply_discount() == 8000.0


def test_getter_name(item1):

    assert item1.name == "Смартфон"


def test_setter_name(item1):

    item1.name = "IPhone 13 Pro"
    assert item1.name == "IPhone 13 P"

    item1.name = "IPhone 13"
    assert item1.name == "IPhone 13"


def test_string_to_number():

    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5