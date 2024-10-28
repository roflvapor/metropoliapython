
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus=0 , kuljettumatka=0 ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = nykynopeus
        self.kuljettumatka = kuljettumatka

    def kiihdytä(self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nykynopeus * tuntimäärä
        print(f"rekkari: {self.rekisteritunnus}, matka: {self.kuljettumatka} km, nopeus: {self.nykynopeus} ")
class Sahkoauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, akkukwh):
        self.akkuwh = akkukwh
        super().__init__(rekisteritunnus, huippunopeus)

class Bensaauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, tank):
        self.tank = tank
        super().__init__(rekisteritunnus, huippunopeus)

#sähköauton (ABC-15, 180 km/h, 52.5 kWh)
#polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).

sahko = Sahkoauto("ABC-15", 180, 52.5)
bensa = Bensaauto("ACD-123", 165,32.3 )
sahko.kiihdytä(350)
bensa.kiihdytä(350)
sahko.kulje(3)
bensa.kulje(3)
