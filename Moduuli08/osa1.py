import mysql.connector

def hae_lentokentat(country):
    sql = f"SELECT name,municipality FROM airport where IDENT='{country}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[0]}. Sijaitseen {rivi[1]} ")
    return


yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='Kevin',
         password='123',
         autocommit=True,
         collation="utf8mb4_unicode_ci"
         )

country = input("anna ICAO koodin: ")
hae_lentokentat(country)