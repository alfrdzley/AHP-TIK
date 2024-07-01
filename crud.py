# file ini akan mengelola operasi CRUD (Create, Read, Update, Delete) pada database.

from database import session, Kriteria, Alternatif

# Fungsi CRUD untuk Kriteria
def tambah_kriteria(nama, bobot):
    kriteria_baru = Kriteria(nama=nama, bobot=bobot)
    session.add(kriteria_baru)
    session.commit()
    print("Kriteria berhasil ditambahkan.")

def baca_kriteria():
    kriteria_list = session.query(Kriteria).all()
    for kriteria in kriteria_list:
        print(f"ID: {kriteria.id}, Nama: {kriteria.nama}, Bobot: {kriteria.bobot}")

def update_kriteria(id, nama=None, bobot=None):
    kriteria = session.query(Kriteria).filter_by(id=id).first()
    if kriteria:
        if nama:
            kriteria.nama = nama
        if bobot:
            kriteria.bobot = bobot
        session.commit()
        print("Kriteria berhasil diupdate.")
    else:
        print("Kriteria tidak ditemukan.")

def hapus_kriteria(id):
    kriteria = session.query(Kriteria).filter_by(id=id).first()
    if kriteria:
        session.delete(kriteria)
        session.commit()
        print("Kriteria berhasil dihapus.")
    else:
        print("Kriteria tidak ditemukan.")

# Fungsi CRUD untuk Alternatif
def tambah_alternatif(nama, skor):
    alternatif_baru = Alternatif(nama=nama, skor=str(skor))
    session.add(alternatif_baru)
    session.commit()
    print("Alternatif berhasil ditambahkan.")

def baca_alternatif():
    alternatif_list = session.query(Alternatif).all()
    for alternatif in alternatif_list:
        print(f"ID: {alternatif.id}, Nama: {alternatif.nama}, Skor: {alternatif.skor}")

def update_alternatif(id, nama=None, skor=None):
    alternatif = session.query(Alternatif).filter_by(id=id).first()
    if alternatif:
        if nama:
            alternatif.nama = nama
        if skor:
            alternatif.skor = str(skor)
        session.commit()
        print("Alternatif berhasil diupdate.")
    else:
        print("Alternatif tidak ditemukan.")

def hapus_alternatif(id):
    alternatif = session.query(Alternatif).filter_by(id=id).first()
    if alternatif:
        session.delete(alternatif)
        session.commit()
        print("Alternatif berhasil dihapus.")
    else:
        print("Alternatif tidak ditemukan.")
