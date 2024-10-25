import random
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

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.osallistujat:
            print("Kilpailija: " + auto.rekisteritunnus, auto.huippunopeus, auto.kuljettumatka, auto.nykynopeus)
        print("")

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.kuljettumatka >= self.pituus:
                return True
        return False



kilpailijat = []
for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    kilpailija = Auto(rekisteritunnus, huippunopeus)
    kilpailijat.append(kilpailija)

kilpailu = Kilpailu("Suuri romuralli", 8000, kilpailijat)

while not kilpailu.kilpailu_ohi():
    for i in range(1, 11):
        continue
    kilpailu.tulosta_tilanne()
    kilpailu.tunti_kuluu()

print("")
print("")
print("")
print("Kilpailu ohi")
kilpailu.tulosta_tilanne()