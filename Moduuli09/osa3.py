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


auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kulje(1.5)

