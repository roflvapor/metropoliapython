from random import randint
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus=0 , kuljettumatka=0 ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = nykynopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, nopeusmuutos):
        self.nykynopeus = self.nykynopeus + nopeusmuutos
        if self.nykynopeus <= 0:
            self.nykynopeus = 0
        elif self.nykynopeus >= self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        print("\nRekisteritunnus: " + self.rekisteritunnus + "\nHuippunopeus: " , self.huippunopeus , "km/h" +"\nNykynopeus: " , self.nykynopeus , "\nKuljettu matka: " , self.kuljettumatka)

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + (self.nykynopeus * tuntimaara)

        print("\nRekisteritunnus: " + self.rekisteritunnus + "\nHuippunopeus: " , self.huippunopeus , "km/h" +"\nNykynopeus: " , self.nykynopeus , "\nKuljettu matka: " , self.kuljettumatka)
autolista = []


for i in range(1,11):
    nimi = str(i)
    autolista.append(Auto("ABC-"+nimi,randint(100,200)))

while True:
    for each in autolista:
        if each.kuljettumatka >= 10000:
            break
        each.kiihdyta(randint(-10,15))
        each.kulje(1)

for each in autolista:
    print(each.rekisteritunnus)
    print(each.huippunopeus)
    print(each.nykynopeus)
    print(each.kuljettumatka)


