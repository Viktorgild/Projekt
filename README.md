# Учебный проект по Python.

# Описание проекта:
Этот проект содержит несколько функций для работы с данными о банковских транзакциях и номерах карт.

## Функции:
1. filter_by_currency: передайте список транзакций и валюту, которую хотите отфильтровать. Получите итератор с соответствующими транзакциями.
2. transaction_descriptions — генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
3. card_number_generator — генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
4. mask_account_card — функция принимает один аргумент — строку, содержащую тип и номер карты или счёта. Возвращает строку с замаскированным номером. Если в строке есть «Счёт», то функция возвращает строку с первыми четырьмя символами и замаскированными последними четырьмя символами номера счёта. В противном случае она возвращает строку с последними 4 символами номера карты и всеми символами до них, кроме последних 16, заменёнными на многоточие.
5. get_date — функция принимает на вход дату и время и выдаёт дату в порядке ДД.ММ.ГГГГ. Она возвращает часть строки перед буквой T в исходном значении даты. Все дефисы в полученной дате заменяются точками.
6. get_mask_account — функция принимает номер счёта и возвращает его маску. Последние четыре символа номера возвращаются без изменений, а остальные символы заменяются на звёздочки. Если функция не получила номер счёта, возвращается None.
7. get_mask_card_number — функция получает номер банковской карты и возвращает его в виде маски. Первые четыре цифры номера возвращаются как есть. Следующие две цифры возвращаются после замены остальных символов на звёздочки. Затем идут четыре звёздочки, и последние четыре цифры номера также возвращаются без изменений.
8. filter_by_state — функция возвращает список словарей по ключу. Она принимает два аргумента: список словарей и состояние (по умолчанию «EXECUTED»). Функция перебирает каждый словарь в списке и проверяет значение ключа «state». Если значение равно переданному состоянию, словарь добавляется в результирующий список.
9. sort_by_date — функция сортирует список словарей по дате. Она принимает два аргумента: список словарей и порядок сортировки (по умолчанию «DESC»). Функция использует встроенную функцию sorted() для сортировки списка на основе значения ключа «date» в каждом словаре. Если порядок сортировки равен «DESC», список сортируется в обратном порядке.
10. csv_lxsx - данных в виде списка словарей, где каждый словарь начинается с новой строки. Это позволяет сделать вывод более структурированным и удобным для чтения.
Эти функции могут быть полезны при работе с финансовыми данными и обработке информации о банковских картах. Они позволяют фильтровать транзакции по валюте, получать описания операций, генерировать номера карт, маскировать номера счетов и банковских карт различными способами, а также сортировать данные по дате и выбирать записи с определённым состоянием.

## Как использовать:
* filter_by_currency: передайте список транзакций и валюту, которую хотите отфильтровать. Получите итератор с соответствующими транзакциями.
* transaction_descriptions: передайте список транзакций. Получите генератор с описаниями операций.
* card_number_generator: укажите диапазон номеров карт. Получите генератор номеров карт в указанном формате.
* mask_account_card: передайте строку с типом и номером карты или счёта. Получите строку с замаскированным номером.
* get_date: передайте дату и время. Получите дату в формате ДД.ММ.ГГГГ.
* get_mask_account: передайте номер счёта. Получите его маску.
* get_mask_card_number: передайте номер банковской карты. Получите её маску.
* filter_by_state: передайте список словарей и желаемое состояние. Получите список словарей с выбранным состоянием.
* sort_by_date: передайте список словарей и желаемый порядок сортировки. Получите отсортированный список словарей.
* csv_lxsx: 
* 1. Данные считываются из файла Excel с помощью функции read_excel, которая возвращает DataFrame.
* 2. Затем данные преобразуются в список словарей с помощью метода to_dict с параметром 'records'.
* 3. Для вывода данных используется функция join с символом новой строки '\n' в качестве параметра end. Это обеспечивает начало каждого словаря с новой строки при выводе.
## Пример использования:
```
transactions = ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])
    filtered_transactions = filter_by_currency(transactions, "USD")
for transaction in filtered_transactions:
    print(transaction)

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)

card_
```

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/Viktorgild/Projekt
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Разработчик:

https://github.com/Viktorgild


