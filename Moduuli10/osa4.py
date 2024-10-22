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

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + (self.nykynopeus * tuntimaara)

autolista = []
class Kilpailu:
    def __init__(self, nimi, pituus, autojenlista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = []
        for each in autojenlista:
            self.autolista.append(Auto())
    #def tunti_kuluu(self,):


for i in range(1,11):
    nimi = str(i)
    autolista.append(Auto("ABC-"+nimi,randint(100,200)))
    i+=1
