import csv

import pandas as pd


def read_csv(file_path):
    with open(file_path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data = []
        for row in reader:
            data.append(row)
    return data


def read_excel(file_path):
    df = pd.read_excel(file_path)
    data_dict = df.to_dict("records")
    return data_dict
