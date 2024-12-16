import csv

import pandas as pd


def read_csv(file_path):
    with open(file_path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data = []
        for row in reader:
            data.append(row)
    return data


file_path = "../data/test_csv.csv"
data_list = read_csv(file_path)

output_string = "\n".join([str(item) for item in data_list])
print(data_list)


def read_excel(file_path):
    df = pd.read_excel(file_path)
    data_dict = df.to_dict("records")
    return data_dict


file_path = "../data/transactions_excel.xlsx"
data_dict_list = read_excel(file_path)

output_string = "\n".join([str(item) for item in data_dict_list])
print(data_dict_list)
