import csv

import pandas as pd


def read_csv(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
    return data


file_path = r"C:\Users\35347\PycharmProjects\Projekt\data\test_csv.csv"
data_list = read_csv(file_path)

output_string = "\n".join([str(item) for item in data_list])
print(output_string)


def read_excel(file_path):
    df = pd.read_excel(file_path)
    data_dict = df.to_dict("records")
    return data_dict


file_path = r"C:\Users\35347\PycharmProjects\Projekt\data\transactions_excel.xlsx"
data_dict_list = read_excel(file_path)

output_string = "\n".join([str(item) for item in data_dict_list])
print(output_string)
