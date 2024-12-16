from unittest.mock import patch

from src.external_api import get_conversion


@patch("requests.get")
def test_get_conversion(mock_get, transaction):
    mock_get.return_valuie.json.return_value = {
        "operationAmount": {"amount": 100, "currency": {"code": "USD"}},
        "anotherOperationAmount": {"amount": 100, "currency": {"code": "RUB"}},
    }

    assert get_conversion(transaction) == 10430.87
