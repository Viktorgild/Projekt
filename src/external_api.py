
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
        return round(result["result"], 2)
    else:
        return round(amount, 2)
print(get_conversion(transaktion))