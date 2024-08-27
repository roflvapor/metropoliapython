import mysql.connector

def hae_lentokentat(country):
    sql = f"SELECT type, COUNT(type) AS maara FROM airport where iso_country='{country}'GROUP by type asc"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]} on {rivi[1]} kappaletta")
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

country = input("anna maa koodin: ")
hae_lentokentat(country)