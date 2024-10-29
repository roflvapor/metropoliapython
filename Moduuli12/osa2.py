import json
import requests
paikka = input("Anna kaupungin nimi koska en osaa etsiä kuntaa: ")


pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid=2534fae64d364953a9f2f39afafea07d"
vastaus = requests.get(pyynto).json()
print(json.dumps(vastaus, indent=2))
print("\n")