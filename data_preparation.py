import pandas as pd

data = pd.read_csv('file_dataset.csv')

print(data.head())

print(data.info())

print(data.isnull().sum())

data_cleaned = data.dropna()

data_cleaned.to_csv('dataset_cleaned.csv', index=False)
