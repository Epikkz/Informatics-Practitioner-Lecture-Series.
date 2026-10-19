import matplotlib.pyplot as plt

# Data untuk visualisasi
kategori = ['Q1', 'Q2', 'Q3', 'Q4']
performa = [65, 82, 78, 95]

# Konfigurasi tampilan grafik (prinsip HCI & Visualisasi yang bersih)
plt.figure(figsize=(8, 4))
plt.plot(kategori, performa, marker='o', color='#2b5c8f', linewidth=2.5, markersize=8)

# Penambahan label dan estetika yang komunikatif
plt.title('Tren Performa Kuartalan Perusahaan', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Kuartal', fontsize=10)
plt.ylabel('Skor Performa (%)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(50, 100)

# Menampilkan grafik
plt.tight_layout()
plt.show()
print("Grafik visualisasi data berhasil dirender.")