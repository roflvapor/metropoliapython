
syote = int(input("Haluatko 1: tallenna uusi lentoasema, 2: hakea lentoasema, 3: lopettaa "))
while syote != 3:
    lentoasemat = {"20":"caca"}
    if syote == 1:
        airfield_icao = input("Anna lentoaseman ICAO koodi: ")
        airfield_name = input("Anna lentoaseman nimi: ")
        if airfield_icao or airfield_name in lentoasemat.keys():
            print("Lentoasema on jo tallennettu!")
        elif airfield_icao or airfield_name not in lentoasemat:
            lentoasemat[airfield_icao] = airfield_name
    if syote == 2:
        airfield_icao = input("Anna lentoaseman ICAO koodi: ")
        for icao,name in lentoasemat:
            if icao == airfield_icao:
                print(f"Lentoaseman nimi on {lentoasemat[icao]}")


    if syote == 3:
        break
    syote = int(input("Haluatko 1: tallenna uusi lentoasema, 2: hakea lentoasema, 3: lopettaa "))
