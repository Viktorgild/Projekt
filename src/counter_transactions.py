from collections import Counter


def get_taransctions_type_count(transactions):
    list_ = []

    for i in transactions:
        list_.append(i.get("description"))

    counter = Counter(list_)
    return counter