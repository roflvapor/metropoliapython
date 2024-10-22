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


autokiihdytys = Auto("ABC-123", 142)
autokiihdytys.kiihdyta(30)
autokiihdytys.kiihdyta(70)
autokiihdytys.kiihdyta(50)
autokiihdytys.kiihdyta(-200)
autokiihdytys = Auto("ABC-123", 142)

