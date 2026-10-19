import concurrent.futures
import time

# Fungsi simulasi pemrosesan data berat untuk satu wilayah lokal
def proses_simulasi_wilayah(id_wilayah):
    print(f"Memulai simulasi HPC untuk Wilayah {id_wilayah}...")
    time.sleep(1)  # Mensimulasikan komputasi berat
    hasil = id_wilayah * 3.14159
    return f"Wilayah {id_wilayah selesai, hasil: {hasil:.2f}}"

# Daftar wilayah yang akan diproses secara paralel
wilayah_list = range(1, 6)

print("--- Memulai Komputasi Paralel (HPC Simulation) ---")
start_time = time.time()

# Menggunakan ThreadPoolExecutor untuk pemrosesan paralel
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    hasil_simulasi = list(executor.map(proses_simulasi_wilayah, wilayah_list))

end_time = time.time()

for res in hasil_simulasi:
    print(res)
print(f"Total waktu eksekusi paralel: {end_time - start_time:.2f} detik")