list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей по ключу"""
    result = []
    for item in list_dict:
        if item["state"] == state:
            result.append(item)
    return result


def sort_by_date(list_dict: list, order: str = True) -> list | True:
    """Функция сортирует список словарей по дате."""
    result = sorted(list_dict, key=lambda x: x["date"], reverse=(order == "DESC"))
    return result
