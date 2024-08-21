import random
def funkt1():
    x = random.randint(1,6)
    print(x)
    return x

y = funkt1()
while y != 6:
    y = funkt1()