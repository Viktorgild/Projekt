
transaktion = {
  "operationAmount": {
    "amount": 100,
    "currency": {
      "code": "USD"
    }
  },
  "anotherOperationAmount": {
    "amount": 100,
    "currency": {
      "code": "RUB"
    }
  }
}

import requests
import os
from dotenv import load_dotenv
import logging
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\external_api.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


load_dotenv()

def get_conversion(transaction: dict) -> float:
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code != "RUB":

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

        headers = {
            "apikey": os.getenv("API_KEY")
        }

        response = requests.request("GET", url, headers=headers)

        result = response.json()
        logger.info(f"Конвертация {amount} {code} в RUB: {result['result']}")
        return round(result["result"], 2)
    else:
        logger.debug(f"Сумма операции уже в рублях: {amount}")
        return round(amount, 2)
print(get_conversion(transaktion))