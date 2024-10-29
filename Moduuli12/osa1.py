import json
import requests

pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto).json()
print("\n")
print(vastaus["value"])