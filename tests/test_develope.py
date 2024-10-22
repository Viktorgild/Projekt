import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state
from src.widget import get_date, mask_account_card


def test_get_mask_card():
    assert get_mask_card_number(1596837868705199) == "1596 83** **** 5199"
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"
    assert get_mask_card_number(123) == "Не правильно указан номер карты"
    assert get_mask_card_number(0) == "Не правильно указан номер карты"
    assert get_mask_card_number("Maestro 1596837868705199") == "Допускаются только цифры"


def test_get_mask_account():
    assert get_mask_account("35383033474447895560") == "**5560"
    assert get_mask_account(123) == "Номер счета указан не верно"
    assert get_mask_account(0) == "Номер счета указан не верно"
    assert get_mask_account("Счет 35383033474447895560") == "Допускаются только цифры"


def date():
    assert get_date("2024-03-11T02:26:18.671407") == "2024.03.11"
    assert get_date("T02:26:18.671407") == "Ошибка, не правильный ввод"
    assert get_date("2024-03-11T02:26:18.671401sdfdf3fsdf17") == "2024.03.11"


def mask_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro  1596 83** **** 5199"
    assert mask_account_card(123) == "Не правильно указан номер"
    assert mask_account_card(0) == "Не правильно указан номер"
    assert mask_account_card("1596837868705199") == "1596 83** **** 5199"


@pytest.fixture
def list_doct() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_state(list_dict: list, stste: str = "CANCELED") -> None:
    if stste == "CANCELED":
        assert filter_by_state(list_dict) == [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
