from crud import tambah_kriteria, baca_kriteria, update_kriteria, hapus_kriteria
from crud import tambah_alternatif, baca_alternatif, update_alternatif, hapus_alternatif
from ahp import proses_ahp

# Contoh penggunaan CRUD dan AHP
# Menambahkan kriteria
tambah_kriteria('Kualitas Pendidikan', 0.5)
tambah_kriteria('Fasilitas', 0.3)
tambah_kriteria('Reputasi', 0.2)

# Membaca kriteria
baca_kriteria()

# Menambahkan alternatif
tambah_alternatif('Universitas A', [0.8, 0.7, 0.9])
tambah_alternatif('Universitas B', [0.6, 0.8, 0.7])

# Membaca alternatif
baca_alternatif()

# Memproses AHP
proses_ahp()
