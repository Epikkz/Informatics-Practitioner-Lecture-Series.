from shapely.geometry import Point, Polygon

# Mendefinisikan titik lokasi pusat (misal: Gudang Utama)
gudang_pusat = Point(106.8272, -6.1751) # Koordinat Jakarta (Longitude, Latitude)

# Mendefinisikan area cakupan wilayah pasar (Polygon sederhana)
area_pasar = Polygon([
    (106.80, -6.15), (106.85, -6.15), 
    (106.85, -6.20), (106.80, -6.20)
])

# Kandidat lokasi toko baru
lokasi_toko_baru = Point(106.83, -6.18)

# Pengecekan spasial: Apakah toko baru berada di dalam area pasar?
is_in_market = area_pasar.contains(lokasi_toko_baru)
# Perhitungan jarak Euclidean sederhana ke gudang pusat
jarak_ke_gudang = gudang_pusat.distance(lokasi_toko_baru) * 111  # Konversi kasar ke kilometer

print(f"Apakah toko baru di dalam area pasar? {'Ya' if is_in_market else 'Tidak'}")
print(f"Perkiraan jarak ke gudang pusat: {jarak_ke_gudang:.2f} km")