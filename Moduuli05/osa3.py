
input1 = int(input("anna kokonaisluku: "))
counter = 0
for i in range(2, input1):
    #i alkaa olemalla 2
    if input1 % i == 0:
        #jos syotetty luku on jaollinen i (2lla) sit syoteluku on jaollinen 1, itellä ja joku numero 1...syoten välillä
        counter += 1
        #muistiin et on jaollinen 3 numerolla ainaski
        if counter == 1:
            #koska 3
            print("ei ole alkuluku")
            break
        #jos ei ollut jaollinen 2:lla
        #sit restart ja nyt i = 3
if counter != 1:
    print("on alkuluku")