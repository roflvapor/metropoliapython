import random
def funkt1(maxnoppa):
    x = random.randint(1,maxnoppa)
    while x != maxnoppa:
        x = random.randint(1,maxnoppa)
        print(x)

funkt1(21)