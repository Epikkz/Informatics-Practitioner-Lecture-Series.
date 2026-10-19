from sklearn.tree import DecisionTreeClassifier

# Data Latihan (Fitur: [Jam Belajar, Kehadiran (%)])
X_train = [
    [2, 60], [4, 80], [1, 50], [5, 95], 
    [3, 70], [6, 90], [1.5, 55], [5.5, 92]
]
# Label Target (0 = Gagal, 1 = Lulus)
y_train = [0, 1, 0, 1, 0, 1, 0, 1]

# Inisialisasi dan pelatihan model Machine Learning
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Data baru untuk diprediksi (Contoh: Siswa belajar 4.5 jam, kehadiran 85%)
data_baru = [[4.5, 85]]
prediksi = model.predict(data_baru)

status = "Lulus" if prediksi[0] == 1 else "Gagal"
print(f"Prediksi kelulusan untuk siswa dengan 4.5 jam belajar dan 85% kehadiran: {status}")