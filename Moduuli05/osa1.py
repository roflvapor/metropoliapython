import random

dice = int(input("Montako arpakuutiota haluat: "))
i = 0
z = 0
for i in range(dice):
    x = random.randint(1,6)
    z += x
    i += 1
    #jos haluat tarkistaa menikö ohjelma oikein
    print("arpa oli", x)
print(z)
