import pandas as pd
import numpy as np

# Data mentah penjualan (mengandung nilai kosong/NaN)
data_mentah = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei'],
    'Penjualan': [1200, np.nan, 1500, 1300, 1800],
    'Wilayah': ['Jakarta', 'Bandung', 'Jakarta', 'Surabaya', 'Surabaya']
}

df = pd.DataFrame(data_mentah)

# 1. Pembersihan Data: Mengisi nilai NaN dengan rata-rata penjualan
df['Penjualan'] = df['Penjualan'].fillna(df['Penjualan'].mean())

# 2. Analisis Data: Agregasi rata-rata penjualan berdasarkan wilayah
analisis_wilayah = df.groupby('Wilayah')['Penjualan'].mean().reset_index()

print("--- Data Setelah Dibersihkan ---")
print(df)
print("\n--- Rata-rata Penjualan per Wilayah ---")
print(analisis_wilayah)