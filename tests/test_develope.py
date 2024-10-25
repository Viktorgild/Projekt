import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(str("1596837868705199")) == "1596 83** **** 5199"
    assert get_mask_card_number(str(1596837868705199)) == "1596 83** **** 5199"
    assert get_mask_card_number(str("646864")) == "6468 64** **** 6864"
    assert get_mask_card_number(str("")) == " ** **** "
    assert get_mask_card_number(str("35383033474447895343434560")) == "3538 30** **** 4560"


def test_get_mask_account() -> None:
    assert get_mask_account(str("73654108430135874305")) == "**4305"
    assert get_mask_account(str(73654108430135874305)) == "**4305"
    assert get_mask_account(str("73654108430")) == "**8430"
    assert get_mask_account(str("73654108430132342342342345874305")) == "**4305"


def test_mask_account_card() -> None:
    assert mask_account_card(str("Maestro 1596837868705199")) == "Maestro  1596 83** **** 5199"
    assert mask_account_card(str("Visa Classic 6831982476737658")) == "Visa Classic  6831 98** **** 7658"
    assert mask_account_card(str("Maestro 159683")) == " Maes tr** **** 9683"
    assert mask_account_card(str("Maestro 159683786870519924436324632463246")) == "Maestro 15968378687051992 4436 32** **** 3246"
    assert mask_account_card(str("Счет 64686473678")) == "Счет **3678"
    assert mask_account_card(str("Счет 64686473678894773453463463469589")) == "Счет **9589"
    assert mask_account_card(str("Счет 64686473678894779589")) == "Счет **9589"
    assert mask_account_card(str("")) == "  ** **** "


def test_get_date() -> None:
    assert get_date(str("2024-03-11T02:26:18.671407")) == "2024.03.11"
    assert get_date(str("241353jlgdkgdgd")) == "241353jlgdkgdgd"
    assert get_date(str("2024-03-11T02:26:18.67142355235fdgdfb07")) == "2024.03.11"
    assert get_date(str("")) == ""
    assert get_date(str("124124-124124-124124:23235sfggf")) == "124124.124124.124124:23235sfggf"
    assert get_date(str("02:26:18.671407T2024.03.11")) == "02:26:18.671407"


def test_sort_by_date(list_dict: str) -> None:
    assert sort_by_date(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '201845103414T08:21:33.419441'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10wegw-14T08:21:33.419441'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': ''}]


@pytest.mark.parametrize(
    "input_data,expected_result", [
        ({"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]),
        ({"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"}, [{"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"}]),
    ]
)
def test_filter_by_state(input_data, expected_result):
    result = filter_by_state([input_data], input_data["state"])
    assert result == expected_result

# Дополнительные проверки
def test_empty_list() -> None:
    result = filter_by_state([], "EXECUTED")
    assert result == []

if __name__ == "__main__":
    pytest.main()
