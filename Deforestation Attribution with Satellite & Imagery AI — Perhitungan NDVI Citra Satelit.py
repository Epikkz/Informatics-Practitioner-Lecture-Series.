import numpy as np

# Simulasi matriks piksel citra satelit (Band NIR dan Red) untuk area hutan
# Nilai piksel berkisar antara 0.0 hingga 1.0
nir_band = np.array([
    [0.8, 0.7, 0.2],  # 0.2 merepresentasikan indikasi area terdeforestasi/tanah kosong
    [0.9, 0.8, 0.7]
])

red_band = np.array([
    [0.1, 0.1, 0.4],
    [0.1, 0.2, 0.2]
])

# Perhitungan rumus NDVI: (NIR - Red) / (NIR + Red)
# Nilai NDVI tinggi (> 0.4) = Hutan lebat, Nilai rendah/negatif = Air, Tanah kosong, atau Deforestasi
ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-8)

print("--- Matriks Hasil Analisis NDVI Citra Satelit ---")
print(np.round(ndvi, 2))

# Analisis sederhana ambang batas (Thresholding) deteksi deforestasi
area_deforestasi = np.sum(ndvi < 0.3)
print(f"\nJumlah piksel terdeteksi mengalami degradasi/deforestasi: {area_deforestasi} piksel")