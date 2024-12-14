import json

import pandas as pd
import pytest

from src.titanic import avg_age_by_gender, fare_per_passenger_by_class, filter_passengers


@pytest.fixture
def titanic_df():
    sample_dict = {
        "PassengerId": [1, 2, 3, 4, 5],
        "Survived": [0, 1, 1, 1, 0],
        "Pclass": [3, 1, 3, 1, 3],
        "Name": ["name1", "name2", "name3", "name4", "name5"],
        "Sex": ["male", "female", "female", "female", "male"],
        "Age": [22.0, 38.0, 26.0, 35.0, 35.0],
        "SibSp": [1, 1, 0, 1, 0],
        "Parch": [0, 0, 0, 0, 0],
        "Ticket": ["tic1", "tic2", "tic3", "tic4", "tic5"],
        "Fare": [7.3, 71.3, 7.9, 53.1, 8.1],
        "Cabin": [None, "C85", None, "C123", None],
        "Embarked": ["S", "C", "S", "S", "S"],
    }
    return pd.DataFrame(sample_dict)


def test_avg_age_by_gender(titanic_df):
    expected_result = {"Мужчины": 28.5, "Женщины": 29.7}
    assert avg_age_by_gender(titanic_df) == json.dumps(expected_result)


def test_filter_passengers(titanic_df):
    expected_result = titanic_df.iloc[1:4].to_json(orient="records")
    assert filter_passengers(titanic_df) == expected_result


def test_fare_per_passenger_by_class(titanic_df):
    expected_result = {"1": 62.2, "3": 7.3}
    assert fare_per_passenger_by_class(titanic_df) == json.dumps(expected_result)
