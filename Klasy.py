from sqlalchemy import Sequence, Column, Integer, String
from geoalchemy2 import Geometry
from baza_danych import *
from geopy.geocoders import Nominatim

def wspolrzedne (address):
    geolocator = Nominatim(user_agent='my_geocoder')
    location = geolocator.geocode(address)

    latitude, longitude = location.latitude, location.longitude
    return latitude, longitude

# KLASY #
class Uczelnia(Base):
    __tablename__ = 'lista_uczelni'

    id = Column(Integer(), Sequence('uczelnia_id_seq'), primary_key=True)
    nazwa = Column(String(100), nullable=False)
    miasto = Column(String(100), nullable=False)
    wojewodztwo = Column(String(100), nullable=False)
    powiat = Column(String(100), nullable=False)
    id_uczelnia = Column(String(100), nullable=False)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=False)

    def __init__(self, nazwa, miasto, wojewodztwo, powiat, id_uczelnia):
        self.nazwa = nazwa
        self.miasto = miasto
        self.wojewodztwo = wojewodztwo
        self.powiat = powiat
        self.id_uczelnia = id_uczelnia
        cordy = wspolrzedne(miasto)
        self.lokalizacja = f'POINT({cordy[1]} {cordy[0]})'

class Pracownicy(Base):
    __tablename__ = 'lista_pracownikow'

    id = Column(Integer(), Sequence('uczelnia_id_seq'), primary_key=True)
    imie = Column(String(100), nullable=False)
    nazwisko = Column(String(100), nullable=False)
    tytul = Column(String(100), nullable=False)
    przedmiot = Column(String(100), nullable=False)
    miasto = Column(String(100), nullable=False)
    wojewodztwo = Column(String(100), nullable=False)
    id_pracownik = Column(String(100), nullable=False)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=False)

    def __init__(self, imie, nazwisko, tytul, przedmiot, miasto, wojewodztwo, id_pracownik):
        self.imie = imie
        self.nazwisko = nazwisko
        self.tytul = tytul
        self.przedmiot = przedmiot
        self.miasto = miasto
        self.wojewodztwo = wojewodztwo
        self.id_pracownik = id_pracownik
        cordy = wspolrzedne(miasto)
        self.lokalizacja = f'POINT({cordy[1]} {cordy[0]})'

class Student(Base):
    __tablename__ = 'lista_studentow'

    id = Column(Integer(), Sequence('student_id_seq'), primary_key=True)
    imie = Column(String(100), nullable=False)
    nazwisko = Column(String(100), nullable=False)
    wiek = Column(Integer(), nullable=False)
    rok = Column(Integer(), nullable=False)
    kierunek = Column(String(100), nullable=False)
    akademik = Column(String(100), nullable=False)
    miasto = Column(String(100), nullable=False)
    id_student = Column(String(100), nullable=False)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=False)

    def __init__(self, imie, nazwisko, wiek, rok, kierunek, akademik, miasto, id_student):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.rok = rok
        self.kierunek = kierunek
        self.akademik = akademik
        self.miasto = miasto
        self.id_student = id_student
        cordy = wspolrzedne(miasto)
        self.lokalizacja = f'POINT({cordy[1]} {cordy[0]})'

Base.metadata.create_all(engine)
