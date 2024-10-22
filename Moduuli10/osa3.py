class Hissi:
    def __init__(self, minfloor, maxfloor):
        self.currentfloor = minfloor
        self.maxfloor = maxfloor
        self.minfloor = minfloor

    def floor_down(self):
        self.currentfloor -= 1

    def floor_up(self):
        self.currentfloor += 1

    def siirry_kerrokseen(self,kerros):
        print("Hetkellä kerroksella: ", self.currentfloor)
        while self.currentfloor != kerros:
            if self.currentfloor < kerros:
                self.floor_up()
                print("Hetkellä kerroksella: ", self.currentfloor)
            if self.currentfloor > kerros:
                self.floor_down()
                print("Hetkellä kerroksella: ", self.currentfloor)
        if self.currentfloor == kerros:
            print("Olet halutulla kerroksella:",self.currentfloor, "\n")
class Talo:
    def __init__(self, minfloor, maxfloor, elevamount):
        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.elevamount = elevamount
        self.elevlist = []
        for i in range(elevamount):
            self.elevlist.append(Hissi(self.minfloor, self.maxfloor))
            i+=1

    def aja_hissiä(self, hissinumber , target):
        h = self.elevlist[hissinumber-1]
        h.siirry_kerrokseen(target)

    def palohälytys(self):
        for each in self.elevlist:
            each.siirry_kerrokseen(self.minfloor)

talo = Talo(1,8,3)
talo.aja_hissiä(1,5)
talo.aja_hissiä(2,5)
talo.aja_hissiä(3,5)
talo.palohälytys()
