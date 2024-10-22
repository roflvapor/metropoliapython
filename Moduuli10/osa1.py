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
            print("Olet halutulla kerroksella:",self.currentfloor,"nyt takas alas.")
            while self.currentfloor > self.minfloor:
                self.floor_down()
                print("Hetkellä kerroksella: ", self.currentfloor)

h = Hissi(1,8)
h.siirry_kerrokseen(5)

