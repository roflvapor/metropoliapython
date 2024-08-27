import mysql.connector
from geopy.distance import geodesic as GD

lista = []


def hae_lentokentat(country, country2):
    sql = f"SELECT * FROM airport where IDENT='{country}'OR IDENT='{country2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista.append(rivi[4])
            lista.append(rivi[5])
    paikka1 = (lista[0], lista[1])
    paikka2 = (lista[2], lista[3])
    print("Etäisyys on: ", GD(paikka1, paikka2).km, "kilometriä")
    return


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='Kevin',
    password='123',
    autocommit=True,
    collation="utf8mb4_unicode_ci"
)

country = "EFVU"
country2 = "EFFO"
# country = input("Anna ICAO koodi 1: ")
# country2 = input("Anna ICAO koodi 2: ")
hae_lentokentat(country, country2)
