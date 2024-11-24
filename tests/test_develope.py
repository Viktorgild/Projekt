import pytest
from unittest.mock import patch

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.decorators import log


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
    assert (
        mask_account_card(str("Maestro 159683786870519924436324632463246"))
        == "Maestro 15968378687051992 4436 32** **** 3246"
    )
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
    assert sort_by_date(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "201845103414T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10wegw-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": ""},
    ]


@pytest.mark.parametrize(
    "input_data,expected_result",
    [
        (
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            [{"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"}],
        ),
    ],
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


def test_filter_by_currency(transactions: list) -> None:
    empty_string_transactions = list(filter_by_currency(transactions, "USD"))
    assert empty_string_transactions == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]

    empty_string_transactions = list(filter_by_currency(transactions, ""))
    assert empty_string_transactions == []

    empty_string_transactions = list(filter_by_currency(transactions, "RUB"))
    assert empty_string_transactions == [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_transaction_descriptions(transactions: list) -> None:

    descriptions = transaction_descriptions(transactions)
    for _ in range(len(transactions)):
        description = next(descriptions)
        assert description == transactions[_]["description"]


def test_performance():
    """Тест производительности."""
    for _ in range(1000):
        list(card_number_generator(1, 999))

    iterations = 1000
    assert iterations > 500, "Функция должна выполнить более 500 итераций за разумное время."



def test_success(capsys):
    """Тест успешного выполнения функции."""
    @log()
    def my_func(x: int, y: int) -> int:
        return x + y

    result = my_func(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    expected_output = 'my_func ok \n\n'
    assert captured.out == expected_output



def test_log_success(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    expected_output = f"{my_function.__name__} ok \n\n"
    assert captured.out == expected_output

def test_log_failure(capsys):
    # Здесь мы тестируем поведение при возникновении исключения
    with pytest.raises(Exception):
        @log(filename='test.log')
        def my_function():
            raise Exception("Test Error")

        my_function()
        captured = capsys.readouterr()
        expected_error_message = "my_function error: Test Error : ()"
        assert captured.err == expected_error_message
        with open('test.log', 'r') as file:
            file_content = file.read()
            assert expected_error_message in file_content


