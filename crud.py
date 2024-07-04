from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Kriteria(Base):
    __tablename__ = 'kriteria'
    id = Column(Integer, primary_key=True)
    nama = Column(String, nullable=False)
    bobot = Column(Float, nullable=False)

class Alternatif(Base):
    __tablename__ = 'alternatif'
    id = Column(Integer, primary_key=True)
    nama = Column(String, nullable=False)
    skor = Column(JSON, nullable=False)  # Menyimpan skor sebagai JSON

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def tambah_kriteria(nama, bobot):
    kriteria = Kriteria(nama=nama, bobot=bobot)
    session.add(kriteria)
    session.commit()

def baca_kriteria():
    kriteria_list = session.query(Kriteria).all()
    for k in kriteria_list:
        print(f"ID: {k.id}, Nama: {k.nama}, Bobot: {k.bobot}")

def update_kriteria(id, nama, bobot):
    kriteria = session.query(Kriteria).get(id)
    if kriteria:
        kriteria.nama = nama
        kriteria.bobot = bobot
        session.commit()

def hapus_kriteria(id):
    kriteria = session.query(Kriteria).get(id)
    if kriteria:
        session.delete(kriteria)
        session.commit()

def tambah_alternatif(nama, skor):
    kriteria_count = session.query(Kriteria).count()
    if len(skor) != kriteria_count:
        raise ValueError(f"Jumlah skor ({len(skor)}) tidak sesuai dengan jumlah kriteria ({kriteria_count})")
    alternatif = Alternatif(nama=nama, skor=skor)
    session.add(alternatif)
    session.commit()

def baca_alternatif():
    alternatif_list = session.query(Alternatif).all()
    for a in alternatif_list:
        print(f"ID: {a.id}, Nama: {a.nama}, Skor: {a.skor}")

def update_alternatif(id, nama, skor):
    kriteria_count = session.query(Kriteria).count()
    if len(skor) != kriteria_count:
        raise ValueError(f"Jumlah skor ({len(skor)}) tidak sesuai dengan jumlah kriteria ({kriteria_count})")
    alternatif = session.query(Alternatif).get(id)
    if alternatif:
        alternatif.nama = nama
        alternatif.skor = skor
        session.commit()

def hapus_alternatif(id):
    alternatif = session.query(Alternatif).get(id)
    if alternatif:
        session.delete(alternatif)
        session.commit()