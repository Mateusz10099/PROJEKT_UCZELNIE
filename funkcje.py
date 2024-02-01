import folium
from Klasy import *
from baza_danych import *

# LOGOWANIE #

def logowanie():
    while True:
        login = input('Login: ')
        hasło = input('Hasło: ')
        if ((login == 'Mateusz')
            and (hasło == '123')):
            GUI()
            break
        else:
            print('Nieprawidłowy login lub hasło')
            print('Spróbuj jeszcze raz')

# FUNKCJE #

def dodaj_pracownika():
    imie = input('Wpisz imie pracownika: ')
    nazwisko = input('Wpisz nazwisko pracownika: ')
    tytul = input('Podaj tytuł naukowy pracownika: ')
    przedmiot = input('Wpisz przedmiot, który prowadzi pracownik: ')
    miasto = input('Podaj miasto pracownika: ')
    wojewodztwo = input('Podaj województwo pracownika: ')
    id_pracownik = input('Wpisz numer uczelni w jakiej pracuje: ')

    add=Pracownicy(imie, nazwisko, tytul, przedmiot, miasto, wojewodztwo, id_pracownik)
    session.add(add)
    session.commit()
def wyswietl_pracownikow():
    wszyscy_pracownicy = session.query(Pracownicy).all()
    if wszyscy_pracownicy == []:
        print('Nie ma jeszcze żadnych dodanych pracowników')
    else:
        for id, pracownik in enumerate(wszyscy_pracownicy):
            print(f"{id+1}. Pracownik {pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko}, uczy przedmiotu {pracownik.przedmiot}. Jest z miasta {pracownik.miasto}. Pracuje w uczelni o numerze {pracownik.id_pracownik}")
def usun_pracownika():
    do_usuniecia = input('Podaj nazwisko pracownika/ów do usunięcia: ')
    wszyscy_pracownicy = session.query(Pracownicy).filter(Pracownicy.nazwisko==do_usuniecia)

    lista = []
    for pracownik in wszyscy_pracownicy:
        if pracownik.nazwisko == do_usuniecia:
            lista.append(pracownik)
        print('Odnalezieni pracownicy: ')
        print('0 - Usuń wszystkich pracowników: ')

    for id, pracownik in enumerate(lista):
        print(f"{id+1}. Pracownik {pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko}, uczy przedmiotu {pracownik.przedmiot}. Jest z miasta {pracownik.miasto}. Pracuje w uczelni o numerze {pracownik.id_pracownik}")
    aaa = int(input('Wybierz pracownika do usunięcia: '))
    if aaa == 0:
        for pracownik in lista:
            session.delete(pracownik)
    else:
        bbb = lista[aaa-1]
        session.delete(bbb)

    session.commit()
def aktualizacja_pracownikow():
    aktualizacja = input('Podaj nazwisko pracownika do zmiany danych: ')
    wszyscy_pracownicy = session.query(Pracownicy).filter(Pracownicy.nazwisko == aktualizacja).all()

    if wszyscy_pracownicy == []:
        print('Nie ma takiego pracownika')
    else:
        for pracownik in wszyscy_pracownicy:
            pracownik.imie = input('Wpisz imie pracownika: ')
            pracownik.nazwisko = input('Wpisz nazwisko pracownika: ')
            pracownik.tytul = input('Podaj tytuł naukowy pracownika: ')
            pracownik.przedmiot = input('Wpisz przedmiot, który prowadzi pracownik: ')
            pracownik.miasto = input('Podaj miasto pracownika: ')
            pracownik.wojewodztwo = input('Podaj województwo pracownika: ')
            pracownik.id_pracownik = input('Wpisz numer uczelni w jakiej pracuje: ')
            pracownik.lokalizacja = f"POINT({wspolrzedne(pracownik.miasto)[1]} {wspolrzedne(pracownik.miasto)[0]})"

    session.commit()
def dodaj_uczelnie():
    nazwa = input('Wpisz nazwę uczelni: ')
    miasto = input('Wpisz miasto, gdzie znajduje się uczelnia: ')
    wojewodztwo = input('Wpisz województwo, gdzie znajduje się uczelnia: ')
    powiat = input('Wpisz powat, gdzie znajduje się uczelnia: ')
    id_uczelnia = input('Podaj numer uczelni: ')

    add=Uczelnia(nazwa, miasto, wojewodztwo, powiat, id_uczelnia)
    session.add(add)
    session.commit()
def wyswietl_uczelnie():
    wszystkie_uczelnie = session.query(Uczelnia).all()
    if wszystkie_uczelnie == []:
        print('Nie ma jeszcze wprowadzonych uczelni')
    else:
        for id, uczelnia in enumerate(wszystkie_uczelnie):
            print(f"{id + 1}. {uczelnia.nazwa}, miasto - {uczelnia.miasto} w województwie {uczelnia.wojewodztwo}, powiat - {uczelnia.powiat}. Uczelnia o numerze {uczelnia.id_uczelnia}")
def usun_uczelnie():
    do_usuniecia = input('Podaj nazwę uczelni do usunięcia: ')
    wszystkie_uczelnie = session.query(Uczelnia).filter(Uczelnia.nazwa == do_usuniecia)

    lista = []
    for uczelnia in wszystkie_uczelnie:
        if uczelnia.nazwa == do_usuniecia:
            lista.append(uczelnia)
        print('Odnalezione Uczelnie: ')
        print('0 - Usuń wszystkie uczelnie: ')

    for id, uczelnia in enumerate(lista):
        print(f"{id + 1}. {uczelnia.nazwa}, miasto - {uczelnia.miasto} w województwie {uczelnia.wojewodztwo}, powiat - {uczelnia.powiat}. Uczelnia o numerze {uczelnia.id_uczelnia}")
    aaa = int(input('Wybierz uczelnie do usunięcia: '))
    if aaa == 0:
        for uczelnia in lista:
            session.delete(uczelnia)
    else:
        bbb = lista[aaa - 1]
        session.delete(bbb)

    session.commit()
def aktualizacja_uczelni():
    aktualizacja = input('Podaj nazwę uczelni do zmiany danych: ')
    wszystkie_uczelnie = session.query(Uczelnia).filter(Uczelnia.nazwa == aktualizacja).all()

    if wszystkie_uczelnie == []:
        print('Nie ma takiej uczelni')
    else:
        for uczelnia in wszystkie_uczelnie:
            uczelnia.nazwa = input('Wpisz nazwę uczelni: ')
            uczelnia.miasto = input('Wpisz miasto, gdzie znajduje się uczelnia: ')
            uczelnia.wojewodztwo = input('Wpisz województwo, gdzie znajduje się uczelnia: ')
            uczelnia.powiat = input('Wpisz powat, gdzie znajduje się uczelnia: ')
            uczelnia.id_uczelnia = input('Podaj numer uczelni: ')
            uczelnia.lokalizacja = f"POINT({wspolrzedne(uczelnia.miasto)[1]} {wspolrzedne(uczelnia.miasto)[0]})"

    session.commit()
def dodaj_studenta():
    imie = input('Wpisz imie studenta: ')
    nazwisko = input('Wpisz nazwisko studenta: ')
    while True:
        try:
            wiek = int(input('Podaj wiek studenta (1-99): '))
            if 1 <= wiek <= 99:
                break
            else:
                print("Wiek musi być liczbą całkowitą z zakresu 1-99.")
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
    while True:
        try:
            rok = int(input('Podaj rok studenta (1-5): '))
            if 1 <= rok <= 5:
                break
            else:
                print("Rok musi być liczbą całkowitą z zakresu 1-5.")
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
    kierunek = input('Podaj kierunek na jakim studiuje: ')
    akademik = input('Podaj akademik w którym mieszka: ')
    miasto = input('Podaj miasto z którego jest: ')
    id_student = input('Wpisz numer uczelni do jakiej uczęszcza: ')

    add = Student(imie, nazwisko, wiek, rok, kierunek, akademik, miasto, id_student)
    session.add(add)
    session.commit()
def wyswietl_studentow():
    wszyscy_studenci = session.query(Student).all()
    if wszyscy_studenci == []:
        print('Nie ma jeszcze wprowadzonych studentów')
    else:
        for id, student in enumerate(wszyscy_studenci):
            print(f"{id + 1}. Student {student.imie} {student.nazwisko}, {student.wiek} lat. Studiuje na uczelni o numerze {student.id_student}. {student.rok} rok na kierunku {student.kierunek}. Zakwaterowany w {student.akademik}. Jest z miasta {student.miasto}.")
def usun_studenta():
    do_usuniecia = input('Podaj nazwisko studenta do usunięcia: ')
    wszyscy_studenci = session.query(Student).filter(Student.nazwisko == do_usuniecia)

    lista = []
    for student in wszyscy_studenci:
        if student.nazwisko == do_usuniecia:
            lista.append(student)
        print('Odnalezieni studenci: ')
        print('0 - Usuń wszystkich studentów: ')

    for id, student in enumerate(lista):
        print(f"{id + 1}. Student {student.imie} {student.nazwisko}, {student.wiek} lat. Studiuje na uczelni o numerze {student.id_student}. {student.rok} rok na kierunku {student.kierunek}. Zakwaterowany w {student.akademik}. Jest z miasta {student.miasto}.")
    aaa = int(input('Wybierz studenta do usunięcia: '))
    if aaa == 0:
        for student in lista:
            session.delete(student)
    else:
        bbb = lista[aaa - 1]
        session.delete(bbb)

    session.commit()
def aktualizacja_studentow():
    aktualizacja = input('Podaj nazwisko studenta do zmiany danych: ')
    wszyscy_studenci = session.query(Student).filter(Student.nazwisko == aktualizacja).all()

    if wszyscy_studenci == []:
        print('Nie ma takiego studenta')
    else:
        for student in wszyscy_studenci:
            student.imie = input('Wpisz imie studenta: ')
            student.nazwisko = input('Wpisz nazwisko studenta: ')
            while True:
                try:
                    student.wiek = int(input('Podaj wiek studenta (1-99): '))
                    if 1 <= student.wiek <= 99:
                        break
                    else:
                        print("Wiek musi być liczbą całkowitą z zakresu 1-99.")
                except ValueError:
                    print("Wprowadź poprawną liczbę całkowitą.")
            while True:
                try:
                    student.rok = int(input('Podaj rok studenta (1-5): '))
                    if 1 <= student.rok <= 5:
                        break
                    else:
                        print("Rok musi być liczbą całkowitą z zakresu 1-5.")
                except ValueError:
                    print("Wprowadź poprawną liczbę całkowitą.")
            student.kierunek = input('Podaj kierunek na jakim studiuje: ')
            student.akademik = input('Podaj akademik w którym mieszka: ')
            student.miasto = input('Podaj miasto z którego jest: ')
            student.id_student = input('Wpisz numer uczelni do jakiej uczęszcza: ')

    session.commit()
def pracownicy_w_powiecie(session):
    powiaty = (
        session.query(Uczelnia.powiat)
        .distinct()
        .order_by(Uczelnia.powiat)
        .all())
    if not powiaty:
        print('Brak danych o powiatach.')
        return
    print('Dostępne powiaty:')
    for powiat in powiaty:
        print(powiat[0])
    wybrany_powiat = input('Podaj nazwę powiatu, dla którego chcesz wyświetlić pracowników: ')

    pracownicy = (
        session.query(Pracownicy)
        .join(Uczelnia, Pracownicy.id_pracownik == Uczelnia.id_uczelnia)
        .filter(Uczelnia.powiat == wybrany_powiat)
        .all())
    if not pracownicy:
        print(f'Brak pracowników w powiecie {wybrany_powiat}')
    else:
        print(f'Pracownicy w powiecie {wybrany_powiat}:')
        for idx, pracownik in enumerate(pracownicy, start=1):
            print(f"{idx+1}. Pracownik {pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko}, uczy przedmiotu {pracownik.przedmiot}. Jest z miasta {pracownik.miasto}. Pracuje w uczelni o numerze {pracownik.id_pracownik}")
def usun_pracownikow_z_powiatu(session):
    powiaty = session.query(Uczelnia.powiat).distinct().all()
    print("Dostępne powiaty:")
    for idx, powiat in enumerate(powiaty):
        print(f"{idx + 1}. {powiat[0]}")
    wybrany_powiat = input("Podaj nazwę powiatu, z którego chcesz usunąć pracowników: ")

    pracownicy_do_usuniecia = (
        session.query(Pracownicy)
        .join(Uczelnia, Pracownicy.id_pracownik == Uczelnia.id_uczelnia)
        .filter(Uczelnia.powiat == wybrany_powiat)
        .all())
    for pracownik in pracownicy_do_usuniecia:
        session.delete(pracownik)

    session.commit()
    print(f"Usunięto pracowników z powiatu {wybrany_powiat}")
def aktualizuj_dane_pracownika_z_powiatu(session):
    powiaty = session.query(Uczelnia.powiat).distinct().all()
    print("Dostępne powiaty:")
    for idx, powiat in enumerate(powiaty):
        print(f"{idx + 1}. {powiat[0]}")
    wybrany_powiat = input("Podaj nazwę powiatu, z którego chcesz usunąć pracowników: ")

    pracownicy_do_aktualizacji = (
        session.query(Pracownicy)
        .join(Uczelnia, Pracownicy.id_pracownik == Uczelnia.id_uczelnia)
        .filter(Uczelnia.powiat == wybrany_powiat)
        .all())

    if not pracownicy_do_aktualizacji:
        print(f"Brak pracowników w powiecie {wybrany_powiat}")
        return
    print("Pracownicy w wybranym powiecie:")
    for idx, pracownik in enumerate(pracownicy_do_aktualizacji, start=1):
        print(f"{idx+1}. Pracownik {pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko}, uczy przedmiotu {pracownik.przedmiot}. Jest z miasta {pracownik.miasto}. Pracuje w uczelni o numerze {pracownik.id_pracownik}")

    index_pracownika = int(input("Wybierz numer pracownika do aktualizacji: ")) - 1
    if 0 <= index_pracownika < len(pracownicy_do_aktualizacji):
        wybrany_pracownik = pracownicy_do_aktualizacji[index_pracownika]

        wybrany_pracownik.imie = input("Nowe imię: ")
        wybrany_pracownik.nazwisko = input("Nowe nazwisko: ")
        wybrany_pracownik.tytul = input("Nowy tytuł: ")
        wybrany_pracownik.przedmiot = input("Nowy przedmiot: ")
        wybrany_pracownik.miasto = input("Nowe miasto: ")
        wybrany_pracownik.wojewodztwo = input("Nowe województwo: ")

        session.commit()
        print(f"Dane pracownika z powiatu {wybrany_powiat} zostały zaktualizowane.")
    else:
        print("Nieprawidłowy numer pracownika.")
def uczelnie_w_wojewodztwie(session):
    wojewodztwa = session.query(Uczelnia.wojewodztwo).distinct().all()
    dostepne_wojewodztwa = [woj[0] for woj in wojewodztwa]

    print("Dostępne województwa:")
    for i, wojewodztwo in enumerate(dostepne_wojewodztwa, start=1):
        print(f"{i}. {wojewodztwo}")
    wybrane_wojewodztwo = input("Podaj nazwę województwa: ")
    uczelnie_w_wojewodztwie = (
        session.query(Uczelnia)
        .filter(Uczelnia.wojewodztwo == wybrane_wojewodztwo)
        .all())

    if not uczelnie_w_wojewodztwie:
        print(f"Brak uczelni w województwie {wybrane_wojewodztwo}")
        return
    print(f"Uczelnie w województwie {wybrane_wojewodztwo}:")
    for idx, uczelnia in enumerate(uczelnie_w_wojewodztwie, start=1):
        print(f"{idx + 1}. {uczelnia.nazwa}, miasto - {uczelnia.miasto} w województwie {uczelnia.wojewodztwo}, powiat - {uczelnia.powiat}.Uczelnia o numerze {uczelnia.id_uczelnia}")
def usun_uczelnie_w_wojewodztwie(session):
    wojewodztwa = session.query(Uczelnia.wojewodztwo).distinct().all()
    dostepne_wojewodztwa = [woj[0] for woj in wojewodztwa]

    print("Dostępne województwa:")
    for idx, wojewodztwo in enumerate(dostepne_wojewodztwa, start=1):
        print(f"{idx}. {wojewodztwo}")
    index_wojewodztwa = int(input("Podaj numer województwa: ")) - 1
    wybrane_wojewodztwo = dostepne_wojewodztwa[index_wojewodztwa]

    uczelnie_do_usuniecia = (
        session.query(Uczelnia)
        .filter(Uczelnia.wojewodztwo == wybrane_wojewodztwo)
        .all())
    for uczelnia in uczelnie_do_usuniecia:
        session.delete(uczelnia)

    session.commit()
    print("Uczelnie zostały usunięte.")
def aktualizuj_dane_o_uczelni_z_woj(session):
    wojewodztwa = session.query(Uczelnia.wojewodztwo).distinct().all()
    dostepne_wojewodztwa = [woj[0] for woj in wojewodztwa]
    print("Dostępne województwa:")
    for idx, wojewodztwo in enumerate(dostepne_wojewodztwa, start=1):
        print(f"{idx}. {wojewodztwo}")

    index_wojewodztwa = int(input("Wybierz numer województwa: ")) - 1
    wybrane_wojewodztwo = dostepne_wojewodztwa[index_wojewodztwa]
    uczelnie = (
        session.query(Uczelnia)
        .filter(Uczelnia.wojewodztwo == wybrane_wojewodztwo)
        .all())
    print(f"Uczelnie w województwie {wybrane_wojewodztwo}:")
    for idx, uczelnia in enumerate(uczelnie, start=1):
        print(f"{idx}. {uczelnia.nazwa}")

    index_uczelni = int(input("Wybierz numer uczelni do edycji: ")) - 1
    wybrana_uczelnia = uczelnie[index_uczelni]

    print("Aktualne dane uczelni:")
    print(f"Nazwa: {wybrana_uczelnia.nazwa}")
    print(f"Miasto: {wybrana_uczelnia.miasto}")
    print(f"Województwo: {wybrana_uczelnia.wojewodztwo}")
    print(f"Powiat: {wybrana_uczelnia.powiat}")
    print(f"ID Uczelni: {wybrana_uczelnia.id_uczelnia}")
    wybrana_uczelnia.nazwa = input("Nowa nazwa uczelni: ")
    wybrana_uczelnia.miasto = input("Nowe miasto: ")
    wybrana_uczelnia.powiat = input("Nowy powiat: ")
    wybrana_uczelnia.id_uczelnia = input("Nowe ID uczelni: ")

    session.commit()
    print("Dane uczelni zostały zaktualizowane.")
def studenci_na_danym_kierunku(session):
    kierunki = session.query(Student.kierunek).distinct().all()
    dostepne_kierunki = [kier[0] for kier in kierunki]

    print("Dostępne kierunki:")
    for i, kierunek in enumerate(dostepne_kierunki, start=1):
        print(f"{i}. {kierunek}")
    wybrany_kierunek = input("Podaj nazwę kierunku: ")
    kierunki_studentow = (
        session.query(Student)
        .filter(Student.kierunek == wybrany_kierunek)
        .all())

    print(f"Studenci na kierunku {wybrany_kierunek}:")
    for idx, student in enumerate(kierunki_studentow, start=1):
        print(f"{idx + 1}. Student {student.imie} {student.nazwisko}, {student.wiek} lat. Studiuje na uczelni o numerze {student.id_student}. {student.rok} rok na kierunku {student.kierunek}. Zakwaterowany w {student.akademik}. Jest z miasta {student.miasto}.")
def usun_studentow_z_kierunku(session):
    kierunki = session.query(Student.kierunek).distinct().all()
    dostepne_kierunki = [kier[0] for kier in kierunki]

    print("Dostępne kierunki:")
    for idx, kierunek in enumerate(dostepne_kierunki, start=1):
        print(f"{idx}. {kierunek}")
    index_kierunku = int(input("Podaj numer kierunku: ")) - 1
    wybrany_kierunek = dostepne_kierunki[index_kierunku]

    studenci_do_usuniecia = (
        session.query(Student)
        .filter(Student.kierunek == wybrany_kierunek)
        .all())
    for student in studenci_do_usuniecia:
        session.delete(student)

    session.commit()
    print("Studenci zostali usunięci.")
def aktualizuj_dane_o_studencie_z_kier(session):
    kierunki = session.query(Student.kierunek).distinct().all()
    dostepne_kierunki = [kierunek[0] for kierunek in kierunki]
    print("Dostępne kierunki:")
    for idx, kierunek in enumerate(dostepne_kierunki, start=1):
        print(f"{idx}. {kierunek}")

    index_kierunku = int(input("Wybierz numer kierunku: ")) - 1
    wybrany_kierunek = dostepne_kierunki[index_kierunku]

    studenci = (
        session.query(Student)
        .filter(Student.kierunek == wybrany_kierunek)
        .all())
    print(f"Studenci na kierunku {wybrany_kierunek}:")
    for idx, student in enumerate(studenci, start=1):
        print(f"{idx}. {student.nazwisko}, {student.imie}")

    index_studenta = int(input("Wybierz numer studenta do edycji: ")) - 1
    wybrany_student = studenci[index_studenta]

    print("Aktualne dane studenta:")
    print(f"Imię: {wybrany_student.imie}")
    print(f"Nazwisko: {wybrany_student.nazwisko}")
    print(f"Wiek: {wybrany_student.wiek}")
    print(f"Rok: {wybrany_student.rok}")
    print(f"Kierunek: {wybrany_student.kierunek}")
    print(f"Akademik: {wybrany_student.akademik}")
    print(f"Miasto: {wybrany_student.miasto}")
    print(f"ID Studenta: {wybrany_student.id_student}")
    wybrany_student.imie = input("Nowe imię studenta: ")
    wybrany_student.nazwisko = input("Nowe nazwisko studenta: ")
    wybrany_student.wiek = int(input("Nowy wiek studenta: "))
    wybrany_student.rok = int(input("Nowy rok studiów: "))
    wybrany_student.kierunek = input("Nowy kierunek studenta: ")
    wybrany_student.akademik = input("Nowy akademik studenta: ")
    wybrany_student.miasto = input("Nowe miasto studenta: ")
    wybrany_student.id_student = input("Nowe ID studenta: ")

    session.commit()
    print("Dane studenta zostały zaktualizowane.")

def mapa_wszystkich_uczelni():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)
    uczelnie = session.query(Uczelnia).all()
    for uczelnia in uczelnie:
        cordy = wspolrzedne(uczelnia.miasto)
        folium.Marker(location=cordy, popup=f"{uczelnia.nazwa}").add_to(mapa)
    print('\n Mapa wszystkich uczelni została wygenerowana')
    mapa.save(f'mapa_uczelni.html')
def mapa_wszystkich_pracownikow():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)
    pracownicy = session.query(Pracownicy).all()
    for pracownik in pracownicy:
        cordy = wspolrzedne(pracownik.miasto)
        folium.Marker(location=cordy, popup=f"{pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko} - {pracownik.przedmiot}").add_to(mapa)
    print('\n Mapa wszystkich pracowników została wygenerowana')
    mapa.save(f'mapa_pracowników.html')

def mapa_pracownikow_z_danej_uczelni():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)
    numer_uczelni = input('Podaj numer uczelni: ')

    pracownicy = session.query(Pracownicy).filter(Pracownicy.id_pracownik == numer_uczelni)
    for pracownik in pracownicy:
        cordy = wspolrzedne(pracownik.miasto)
        folium.Marker(location=cordy,popup=f"{pracownik.tytul}. {pracownik.imie} {pracownik.nazwisko} - {pracownik.przedmiot}").add_to(mapa)
    print(f'Wygenerowano mapę wszystkich pracowników dla uczelni nr {pracownik.id_pracownik}')
    mapa.save(f'mapa_pracowników_z_uczelni.html')

def mapa_studentow_z_danego_kierunku():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)
    kierunek = input('Podaj kierunek: ')

    studenci = session.query(Student).filter(Student.kierunek == kierunek)
    for student in studenci:
        cordy = wspolrzedne(student.miasto)
        folium.Marker(location=cordy,popup=f"{student.imie} {student.nazwisko} - {student.kierunek}").add_to(mapa)
    print(f'Wygenerowano mapę wszystkich pracowników dla uczelni nr {student.kierunek}')
    mapa.save(f'mapa_studentów_z_kierunku.html')

def GUI():
    while True:
        print('\nSystem zarządzania uczelniami w mieście i studentami\n'
              f'0 - Wyłącz program\n'
              f'1 - Dodaj pracownika\n'
              f'2 - Wyświetl wszystkich pracowników\n'
              f'3 - Usuń pracownika\n'
              f'4 - Aktualizuj informacje o pracowniku\n'
              f'5 - Dodaj uczelnie\n'
              f'6 - Wyświetl wszystkie uczelnie\n'
              f'7 - Usuń uczelnie\n'
              f'8 - Aktualizuj informacje o uczelni\n'
              f'9 - Dodaj studenta\n'
              f'10 - Wyświetl wszystkich studentów\n'
              f'11 - Usuń studenta\n'
              f'12 - Aktualizuj informacje o studencie\n'
              f'13 - Wyświetl pracowników z wszystkich uczelni w danym powiecie\n'
              f'14 - Usuń pracowników z wszystkich uczelni w danym powiecie\n'
              f'15 - Aktualizuj pracowników z wybranego powiatu\n'
              f'16 - Wyświetl uczelnie w danym województwie\n'
              f'17 - Usuń uczelnie z danego województwa\n'
              f'18 - Aktualizuj uczelnie z wybranego województwa\n'
              f'19 - Wyświetl studentów z danego kierunku\n'
              f'20 - Usuń studentów z danego kierunku\n'
              f'21 - Aktualizuj studentów z wybranego kierunku\n'
              f'22 - Wyświetl mapę wszystkich uczelni\n'
              f'23 - Wyświetl mapę wszystkich pracowników\n'
              f'24 - Wyświetl mapę pracowników z danej uczelni\n'
              f'25 - Wyświetl mapę studentów z danego kierunku\n')

        option = int(input('Wybierz czynność: '))
        print(f'Funkcja - {option}\n')

        match option:
            case 0:
                print('Kończę pracę')
                break
            case 1:
                print('Dodajesz nowego pracownika')
                dodaj_pracownika()
            case 2:
                print('Wyświetlam listę wszystkich pracowników')
                wyswietl_pracownikow()
            case 3:
                print('Usuwanie pracownika')
                usun_pracownika()
            case 4:
                print('Aktualizacja informacji o pracowniku')
                aktualizacja_pracownikow()
            case 5:
                print('Dodawanie uczelni')
                dodaj_uczelnie()
            case 6:
                print('Wyświetlam listę wszystkich uczelni')
                wyswietl_uczelnie()
            case 7:
                print('Usuwanie uczelni')
                usun_uczelnie()
            case 8:
                print('Aktualizacja informacji o uczelni')
                aktualizacja_uczelni()
            case 9:
                print('Dodajesz nowego studenta')
                dodaj_studenta()
            case 10:
                print('Wyświetlam listę wszystkich studentów')
                wyswietl_studentow()
            case 11:
                print('Usuwanie studentów')
                usun_studenta()
            case 12:
                print('Aktualizacja informacji o studencie')
                aktualizacja_studentow()
            case 13:
                print('Wyświetlam listę pracowników z wszystkich uczelni w wybranym powiecie')
                pracownicy_w_powiecie(session)
            case 14:
                print('Usuwanie pracowników z wszystkich uczelni w danym powiecie ')
                usun_pracownikow_z_powiatu(session)
            case 15:
                print('Aktualizacja pracowników z wybranego powatu')
                aktualizuj_dane_pracownika_z_powiatu(session)
            case 16:
                print('Wyświetlam listę uczelni w danym województwie')
                uczelnie_w_wojewodztwie(session)
            case 17:
                print('Usuwanie uczelni w danym województwie')
                usun_uczelnie_w_wojewodztwie(session)
            case 18:
                print('Aktualizacja uczelni z wybranego województwa')
                aktualizuj_dane_o_uczelni_z_woj(session)
            case 19:
                print('Wyświetlam listę studentów z danego kierunku')
                studenci_na_danym_kierunku(session)
            case 20:
                print('Usuwanie studentów z danego kierunku')
                usun_studentow_z_kierunku(session)
            case 21:
                print('Aktualizacja studentów z danego kierunku')
                aktualizuj_dane_o_studencie_z_kier(session)
            case 22:
                mapa_wszystkich_uczelni()
            case 23:
                mapa_wszystkich_pracownikow()
            case 24:
                mapa_pracownikow_z_danej_uczelni()
            case 25:
                mapa_studentow_z_danego_kierunku()

