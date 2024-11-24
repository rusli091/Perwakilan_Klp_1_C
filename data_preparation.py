import pandas as pd

# Memuat dataset
data = pd.read_csv('file_dataset.csv')

# Menampilkan 5 baris pertama dari dataset
print(data.head())

# Memeriksa informasi dataset
print(data.info())

# Memeriksa nilai yang hilang
print(data.isnull().sum())

# Menghapus baris dengan nilai yang hilang (jika ada)
data_cleaned = data.dropna()

# Menyimpan dataset yang sudah dibersihkan
data_cleaned.to_csv('dataset_cleaned.csv', index=False)
