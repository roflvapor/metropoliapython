
syote = int(input("\nHaluatko 1: tallenna uusi lentoasema, 2: hakea lentoasema, 3: lopettaa "))
lentoasemat = {}

while syote != 3:
    if syote == 1:
        airfield_icao = input("Anna lentoaseman ICAO koodi: ")
        airfield_name = input("Anna lentoaseman nimi: ")
        if airfield_icao in lentoasemat:
            print("Lentoasema on jo tallennettu!")
        elif airfield_icao not in lentoasemat:
            lentoasemat[airfield_icao] = airfield_name
    if syote == 2:
        airfield_icao = input("Anna lentoaseman ICAO koodi: ")
        for icao in lentoasemat:
            if icao == airfield_icao:
                print(f"Lentoaseman nimi on {lentoasemat[icao]}")

    syote = int(input("\nHaluatko 1: tallenna uusi lentoasema, 2: hakea lentoasema, 3: lopettaa "))
