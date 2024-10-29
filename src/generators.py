def filter_by_currency(transactions, currency):
    ''' функция, которая принимает на вход список словарей, представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).'''
    return (transaction for transaction in transactions if transaction['operationAmount']['currency']['code'] == currency)


def transaction_descriptions(transactions):
    ''' генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.'''
    for transaction in transactions:
        yield transaction['description']



def card_number_generator(start, end):
    '''генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.'''
    for i in range(start, end + 1):
        card_num = str(i).zfill(16)
        yield card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]

