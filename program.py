import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AHP:
    def __init__(self, matriks_perbandingan):
        self.matriks_perbandingan = matriks_perbandingan
        self.bobot_kriteria = None
        self.rasio_konsistensi = None

    def hitung_bobot(self):
        # Normalisasi matriks perbandingan berpasangan
        jumlah_kolom = np.sum(self.matriks_perbandingan, axis=0)
        matriks_normalisasi = self.matriks_perbandingan / jumlah_kolom

        # Hitung vektor prioritas (rata-rata baris dalam matriks normalisasi)
        self.bobot_kriteria = np.mean(matriks_normalisasi, axis=1)

        # Hitung Rasio Konsistensi (CR)
        vektor_jumlah_tertimbang = np.dot(self.matriks_perbandingan, self.bobot_kriteria)
        lambda_max = np.mean(vektor_jumlah_tertimbang / self.bobot_kriteria)
        n = len(self.bobot_kriteria)
        CI = (lambda_max - n) / (n - 1)
        RI = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}  # Indeks Konsistensi Acak
        self.rasio_konsistensi = CI / RI[n]

        return self.bobot_kriteria, self.rasio_konsistensi

class Alternatif:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor

    def hitung_skor_akhir(self, bobot_kriteria):
        self.skor_akhir = np.dot(self.skor, bobot_kriteria)
        return self.skor_akhir

def konversi_ke_float(nilai):
    try:
        return float(eval(nilai))
    except:
        return float(nilai)

# Membaca data dari file CSV
df_kriteria = pd.read_csv("kriteria.csv", index_col=0)
df_alternatif = pd.read_csv("alternatif.csv", index_col=0)

# Konversi nilai pada matriks kriteria menjadi float
matriks_perbandingan_kriteria = df_kriteria.applymap(konversi_ke_float).values

# Inisialisasi AHP
ahp = AHP(matriks_perbandingan_kriteria)
bobot_kriteria, rasio_konsistensi = ahp.hitung_bobot()

# Proses data alternatif
alternatif_list = []
for idx, row in df_alternatif.iterrows():
    alternatif_list.append(Alternatif(idx, row.values.astype(float)))

# Hitung skor akhir untuk setiap alternatif
for alternatif in alternatif_list:
    alternatif.hitung_skor_akhir(bobot_kriteria)

# Buat DataFrame untuk hasil
data_kriteria = {
    "Kriteria": df_kriteria.columns,
    "Bobot": bobot_kriteria
}

data_alternatif = {
    "Alternatif": [alt.nama for alt in alternatif_list],
    "Skor Akhir": [alt.skor_akhir for alt in alternatif_list]
}

df_hasil_kriteria = pd.DataFrame(data_kriteria)
df_hasil_alternatif = pd.DataFrame(data_alternatif)

# Tulis ke file CSV
df_hasil_kriteria.to_csv("hasil_bobot_kriteria.csv", index=False)
df_hasil_alternatif.to_csv("hasil_skor_alternatif.csv", index=False)

# Tampilkan ringkasan statistik
statistik_kriteria = df_hasil_kriteria.describe()
statistik_alternatif = df_hasil_alternatif.describe()

# Cetak ringkasan statistik
print("Statistik Kriteria:")
print(statistik_kriteria)
print("\nStatistik Alternatif:")
print(statistik_alternatif)

# Plot statistik bobot kriteria
plt.figure(figsize=(15, 7))

# Diagram batang untuk bobot kriteria
plt.subplot(1, 2, 1)
plt.bar(df_hasil_kriteria["Kriteria"], df_hasil_kriteria["Bobot"], color='blue')
plt.title("Bobot Kriteria")
plt.xlabel("Kriteria")
plt.ylabel("Bobot")
plt.xticks(rotation=45, ha="right")

# Diagram batang untuk skor akhir alternatif
plt.subplot(1, 2, 2)
plt.bar(df_hasil_alternatif["Alternatif"], df_hasil_alternatif["Skor Akhir"], color='green')
plt.title("Skor Akhir Alternatif")
plt.xlabel("Alternatif")
plt.ylabel("Skor Akhir")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()
