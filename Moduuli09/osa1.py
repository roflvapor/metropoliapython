class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus=0 , kuljettumatka=0 ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = nykynopeus
        self.kuljettumatka = kuljettumatka
        print("\nRekisteritunnus: " + self.rekisteritunnus + "\nHuippunopeus: " , self.huippunopeus , "km/h" +"\nNykynopeus: " , self.nykynopeus , "\nKuljettu matka: " , self.kuljettumatka)

Auto("ABC-123",142)

