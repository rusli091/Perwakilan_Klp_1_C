import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset_cleaned.csv')

print("Kolom yang tersedia:")
print(data.columns)

print("\nStatistik deskriptif:")
print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data[data.columns[0]], bins=30, kde=True)
plt.title('Distribusi Kolom Target')
plt.xlabel('Kolom Target')
plt.ylabel('Frekuensi')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data.columns[0], y=data.columns[1], data=data)
plt.title('Hubungan antara Kolom X dan Kolom Y')
plt.xlabel('Kolom X')
plt.ylabel('Kolom Y')
plt.show()

plt.figure(figsize=(12, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Matriks Korelasi')
plt.show()