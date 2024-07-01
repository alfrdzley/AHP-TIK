# File ini berfungsi mengelola model database yang akan digunakan

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Buat engine SQLite
engine = create_engine('sqlite:///database_kampus.db', echo=True)

# Base class untuk class yang akan kita buat
Base = declarative_base()

# Definisikan class untuk tabel kriteria dan alternatif
class Kriteria(Base):
    __tablename__ = 'kriteria'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    bobot = Column(Float)

class Alternatif(Base):
    __tablename__ = 'alternatif'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    skor = Column(String)  # Menyimpan skor sebagai string JSON

# Buat tabel di database
Base.metadata.create_all(engine)

# Buat session
Session = sessionmaker(bind=engine)
session = Session()
