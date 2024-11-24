# Tugas Studi Kasus_Bahan_Presentasi
Nama : Muh.Rusli
Kelas : C
Nim : 60900122074

# Panduan Setup Analisis Data untuk VS Code

Repository ini berisi script Python untuk persiapan data dan analisis data eksploratori (EDA).

### 1. Menyiapkan Lingkungan

1. Untuk menjalankan projek dulu anda harus menclone projek ini:
   ```bash
   git clone https://github.com/username/nama-repository.git
   ```

2. Instal dependensi project menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Menjalankan Script

Untuk menjalankan script persiapan data dan EDA:

```bash
python data_preparation.py
python eda.py
```

## Struktur Project

```
project/
│
├── data_preparation.py
├── eda.py              
└── requirements.txt    
```

## Catatan
- Pastikan semua file data yang diperlukan berada di direktori yang benar sebelum menjalankan script
- Periksa pemilihan interpreter Python di VS Code sesuai dengan lingkungan Anda
- Gunakan terminal terintegrasi VS Code untuk menjalankan perintah

## Pemecahan Masalah
Jika Anda mengalami masalah:
1. Verifikasi semua dependensi telah terinstal dengan benar
2. Periksa apakah path Python sudah diatur dengan benar di VS Code
3. Pastikan semua file yang diperlukan ada di direktori project