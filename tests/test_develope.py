import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_dict() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(list_dict: list, state: str = "EXECUTED") -> None:
    if state == "EXECUTED":
        assert filter_by_state(list_dict) == [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    elif state == "CANCELED":
        assert filter_by_state(list_dict) == [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    elif state == 1234:
        assert filter_by_state(list_dict) == [{"id": 594226727, "state": 1234, "date": "2018-09-12T21:27:25.241689"}]
    elif state == "qwerty":
        assert filter_by_state(list_dict) == [
            {"id": 594226727, "state": "qwerty", "date": "2018-09-12T21:27:25.241689"}
        ]
    elif state == "":
        assert filter_by_state(list_dict) == []


@pytest.fixture
def list_dictt() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": 1234, "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "qwerty", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_sort_by_date(list_dictt: list, sort_order: bool = True) -> None:
    if sort_order:
        assert sort_by_date(list_dictt) == [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "state": 1234, "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "state": "qwerty", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
#