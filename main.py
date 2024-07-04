from crud import tambah_kriteria, tambah_alternatif, baca_kriteria, baca_alternatif
from ahp import proses_ahp


# Tambahkan kriteria
tambah_kriteria("Biaya", 1/3)
tambah_kriteria("Fasilitas", 3)
tambah_kriteria("Kualitas", 1)

# Tambahkan alternatif dengan skor
tambah_alternatif("Kampus A", [0.2, 0.4, 0.4])
tambah_alternatif("Kampus B", [0.4, 0.3, 0.3])
tambah_alternatif("Kampus C", [0.4, 0.3, 0.3])

# Baca data kriteria dan alternatif
baca_kriteria()
baca_alternatif()

# Proses AHP
proses_ahp()