import csv
import pandas as pd



with open(r'C:\Users\35347\PycharmProjects\Projekt\data\test_csv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)



df = pd.read_excel(r'C:\Users\35347\PycharmProjects\Projekt\data\transactions_excel.xlsx')
print(df)