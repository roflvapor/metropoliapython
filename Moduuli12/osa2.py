import json
import requests

paikka = input("Anna kaupungin nimi koska en osaa etsiä kuntaa: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid=2534fae64d364953a9f2f39afafea07d"
pyyntokelv = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid=2534fae64d364953a9f2f39afafea07d&units=metric"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        vastaus = requests.get(pyynto).json()
        print(vastaus["main"]["temp"], "Kelviniä")
        vastaus2 = requests.get(pyyntokelv)
        if vastaus2.status_code == 200:
            vastaus2 = requests.get(pyyntokelv).json()
            print(vastaus2["main"]["temp"], "Celsius")
            print(vastaus2["weather"][0]["description"], "on säätila")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
